# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['def_device', 'Dataset', 'DataLoaders', 'get_dls', 'to_device', 'to_cpu', 'CancelFitException', 'CancelBatchException',
           'CancelEpochException', 'Callback', 'with_cbs', 'run_cbs', 'Learner', 'TrainLearner', 'DeviceCB',
           'SingleBatchCB', 'TrainCB', 'MetricsCB', 'ProgressCB', 'LRFinderCB', 'lr_find', 'show_image', 'subplots',
           'get_grid', 'show_images', 'Hook', 'append_stats', 'Hooks', 'HooksCallback', 'get_hist', 'get_min',
           'ActivationStats', 'clean_ipython_hist', 'clean_tb', 'clean_mem', 'init_weights', 'GeneralRelu']

# %% ../nbs/00_core.ipynb 3
import math
import matplotlib.pyplot as plt
import numpy as np
import sys, gc, traceback
from collections.abc import Mapping
from operator import attrgetter
from copy import copy
from functools import partial
from typing import Any, Literal, Optional, Sequence

import torch
import torch.nn.functional as F
import torch.nn as nn
from torch.nn import init
from torch import optim
from torch.optim.lr_scheduler import ExponentialLR

from torcheval.metrics import BinaryAccuracy, Mean, BinaryAUROC
from torcheval.metrics.functional import binary_auroc, binary_accuracy
from torchmetrics.classification import BinaryMatthewsCorrCoef

import fastcore.all as fc
from fastprogress import progress_bar, master_bar

# %% ../nbs/00_core.ipynb 40
class Dataset():
    "Combines features and lables in a dataset."
    def __init__(self, x, y): self.x, self.y = x, y
    def __len__(self): return len(self.x)
    def __getitem__(self, i): return self.x[i], self.y[i]

# %% ../nbs/00_core.ipynb 43
class DataLoaders():
    "Combines training and validation data in a DataLoaders object that can be passed to a learner."
    def __init__(self, *dls): self.train, self.valid = dls[:2]

# %% ../nbs/00_core.ipynb 44
from torch.utils.data import DataLoader

# %% ../nbs/00_core.ipynb 45
def get_dls(train_ds, valid_ds, bs=32):
    "Turn training and validation set into a DataLoaders object."
    train_dl = DataLoader(train_ds, bs, shuffle=True)
    valid_dl = DataLoader(valid_ds, bs, shuffle=False)
    return DataLoaders(train_dl, valid_dl)

# %% ../nbs/00_core.ipynb 51
def_device = 'mps' if torch.backends.mps.is_available() else 'cuda' if torch.cuda.is_available() else 'cpu'

def to_device(x, device=def_device):
    if isinstance(x, Mapping): return {k:v.to(device) for k, v in x.items()}
    return type(x)(o.to(device) for o in x)

# %% ../nbs/00_core.ipynb 53
def to_cpu(x):
    if isinstance(x, Mapping): return {k:to_cpu(v) for k,v in x.items()}
    if isinstance(x, list): return [to_cpu(o) for o in x]
    if isinstance(x, tuple): return tuple(to_cpu(list(x)))
    res = x.detach().cpu()
    return res.float() if res.dtype==torch.float16 else res

# %% ../nbs/00_core.ipynb 55
class CancelFitException(Exception): pass
class CancelBatchException(Exception): pass
class CancelEpochException(Exception): pass

# %% ../nbs/00_core.ipynb 57
class Callback(): order = 0

# %% ../nbs/00_core.ipynb 59
class with_cbs:
    def __init__(self, nm): self.nm = nm
    def __call__(self, f):
        def _f(o, *args, **kwargs):
            try:
                o.callback(f'before_{self.nm}')
                f(o, *args, **kwargs)
                o.callback(f'after_{self.nm}')
            except globals()[f'Cancel{self.nm.title()}Exception']: pass
            finally: o.callback(f'cleanup_{self.nm}')
        return _f

# %% ../nbs/00_core.ipynb 61
def run_cbs(cbs, method_nm, learn=None):
    for cb in sorted(cbs, key=attrgetter('order')):
        method = getattr(cb, method_nm, None)
        if method is not None: method(learn)

# %% ../nbs/00_core.ipynb 63
class Learner():
    def __init__(self, model, dls=(0,), loss_func=F.mse_loss, lr=0.1, cbs=None, opt_func=optim.SGD):
        cbs = fc.L(cbs)
        fc.store_attr()

    @with_cbs('batch')
    def _one_batch(self):
        self.predict()
        self.callback('after_predict')
        self.get_loss()
        self.callback('after_loss')
        if self.training:
            self.backward()
            self.callback('after_backward')
            self.step()
            self.callback('after_step')
            self.zero_grad()

    @with_cbs('epoch')
    def _one_epoch(self):
        for self.iter,self.batch in enumerate(self.dl): self._one_batch()

    def one_epoch(self, training):
        self.model.train(training)
        self.dl = self.dls.train if training else self.dls.valid
        self._one_epoch()

    @with_cbs('fit')
    def _fit(self, train, valid):
        for self.epoch in self.epochs:
            if train: self.one_epoch(True)
            if valid: torch.no_grad()(self.one_epoch)(False)

    def fit(self, n_epochs=1, train=True, valid=True, cbs=None, lr=None):
        cbs = fc.L(cbs)
        # `add_cb` and `rm_cb` were added in lesson 18
        for cb in cbs: self.cbs.append(cb)
        try:
            self.n_epochs = n_epochs
            self.epochs = range(n_epochs)
            if lr is None: lr = self.lr
            if self.opt_func: self.opt = self.opt_func(self.model.parameters(), lr)
            self._fit(train, valid)
        finally:
            for cb in cbs: self.cbs.remove(cb)

    def __getattr__(self, name):
        if name in ('predict','get_loss','backward','step','zero_grad'): return partial(self.callback, name)
        raise AttributeError(name)

    def callback(self, method_nm): run_cbs(self.cbs, method_nm, self)
    
    @property
    def training(self): return self.model.training

# %% ../nbs/00_core.ipynb 65
class TrainLearner(Learner):
    def predict(self): self.preds = self.model(self.batch[0])
    def get_loss(self): self.loss = self.loss_func(self.preds, self.batch[1])
    def backward(self): self.loss.backward()
    def step(self): self.opt.step()
    def zero_grad(self): self.opt.zero_grad()

# %% ../nbs/00_core.ipynb 67
class DeviceCB(Callback):
    def __init__(self, device=def_device): fc.store_attr()
    def before_fit(self, learn): learn.model.to(self.device)
    def before_batch(self, learn): learn.batch = to_device(learn.batch, device=self.device)

# %% ../nbs/00_core.ipynb 69
class SingleBatchCB(Callback):
    order = 1
    def after_batch(self, learn): raise CancelFitException()

# %% ../nbs/00_core.ipynb 71
class TrainCB(Callback):
    def __init__(self, n_inp=1): self.n_inp = n_inp
    def predict(self, learn): learn.preds = learn.model(*learn.batch[:self.n_inp])
    def get_loss(self, learn): learn.loss = learn.loss_func(learn.preds, *learn.batch[self.n_inp:])
    def backward(self, learn): learn.loss.backward()
    def step(self, learn): learn.opt.step()
    def zero_grad(self, learn): learn.opt.zero_grad()

# %% ../nbs/00_core.ipynb 73
class MetricsCB(Callback):
    def __init__(self, *ms, **metrics):
        for o in ms: metrics[type(o).__name__] = o
        self.metrics = metrics
        self.all_metrics = copy(metrics)
        self.all_metrics["loss"] = self.loss = Mean()

    def _log(self, d): print(d)
    def before_fit(self, learn): learn.metrics = self
    def before_epoch(self, learn): [o.reset() for o in self.all_metrics.values()]
    def after_epoch(self, learn): 
        log = {k:f"{v.compute():.3f}" for k, v in self.all_metrics.items()}
        log['epoch'] = learn.epoch
        log['train'] = 'train' if learn.model.training else 'eval'
        log = {k: str(v) for k, v in log.items()}
        self._log(log)
    
    def after_batch(self, learn):
        x, y = to_cpu(learn.batch)
        for m in self.metrics.values(): m.update(to_cpu(learn.preds), y)
        self.loss.update(to_cpu(learn.loss), weight=len(x))

# %% ../nbs/00_core.ipynb 74
class ProgressCB(Callback):
    order = MetricsCB.order+1
    def __init__(self, plot=False): self.plot = plot
    def before_fit(self, learn):
        learn.epochs = self.mbar = master_bar(learn.epochs)
        self.first = True
        if hasattr(learn, 'metrics'): learn.metrics._log = self._log
        self.losses = []
        self.val_losses = []

    def _log(self, d):
        if self.first:
            self.mbar.write(list(d), table=True)
            self.first = False
        self.mbar.write(list(d.values()), table=True)

    def before_epoch(self, learn): learn.dl = progress_bar(learn.dl, leave=False, parent=self.mbar)
    def after_batch(self, learn):
        learn.dl.comment = f'{learn.loss:.3f}'
        if self.plot and hasattr(learn, 'metrics') and learn.training:
            self.losses.append(learn.loss.item())
            if self.val_losses: self.mbar.update_graph([[fc.L.range(self.losses), self.losses],[fc.L.range(learn.epoch).map(lambda x: (x+1)*len(learn.dls.train)), self.val_losses]])
    
    def after_epoch(self, learn): 
        if not learn.training:
            if self.plot and hasattr(learn, 'metrics'): 
                self.val_losses.append(learn.metrics.all_metrics['loss'].compute())
                self.mbar.update_graph([[fc.L.range(self.losses), self.losses],[fc.L.range(learn.epoch+1).map(lambda x: (x+1)*len(learn.dls.train)), self.val_losses]])

# %% ../nbs/00_core.ipynb 76
class LRFinderCB(Callback):
    def __init__(self, gamma=1.3, max_mult=3, av_over=1): fc.store_attr()
    
    def before_fit(self, learn):
        self.sched = ExponentialLR(learn.opt, self.gamma)
        self.lrs, self.losses = [],[]
        self.losses_tmp = []
        self.count = 0
        self.min = math.inf

    def after_batch(self, learn):
        self.count += 1
        if not learn.training: raise CancelEpochException()
        loss = to_cpu(learn.loss)
        self.losses_tmp.append(loss)
        if loss < self.min: self.min = loss
        if math.isnan(loss) or (loss > self.min*self.max_mult):
            raise CancelFitException()
        if self.count == self.av_over:
            self.lrs.append(learn.opt.param_groups[0]['lr'])
            self.losses.append(np.mean(self.losses_tmp))
            self.losses_tmp = []
            self.count = 0
            self.sched.step()

    def cleanup_fit(self, learn):
        plt.plot(self.lrs, self.losses)
        plt.title('Learning Rate Finder')
        plt.xlabel('learning rate')
        plt.ylabel('loss')
        plt.xscale('log')

# %% ../nbs/00_core.ipynb 77
@fc.patch
def lr_find(self:Learner, gamma=1.3, max_mult=3, start_lr=1e-5, max_epochs=10, av_over=1):
    self.fit(max_epochs, lr=start_lr, cbs=LRFinderCB(gamma=gamma, max_mult=max_mult, av_over=av_over))

# %% ../nbs/00_core.ipynb 79
@fc.delegates(plt.Axes.imshow)
def show_image(im, ax=None, figsize=None, title=None, noframe=True, **kwargs):
    "Show a PIL or PyTorch image on `ax`."
    if fc.hasattrs(im, ("cpu", "permute")):
        im = im.cpu()
        if len(im.shape)==3 and im.shape[0]<5: im = im.permute(1,2,0)
    elif not isinstance(im, np.ndarray): im=np.array(im)
    if im.shape[-1]==1: im = im[..., 0]
    if ax is None: _, ax = plt.subplots(figsize=figsize)
    ax.imshow(im, **kwargs)
    if title is not None: ax.set_title(title)
    ax.set_xticks([]) 
    ax.set_yticks([]) 
    if noframe: ax.axis('off')
    return ax

# %% ../nbs/00_core.ipynb 80
@fc.delegates(plt.subplots, keep=True)
def subplots(
    nrows=1, # Number of rows in returned axes grid
    ncols=1, # Number of columns in retruned axes grid
    figsize=None, # Width, height in inches of the returned figure
    imsize=3, # Size (in inches) of images that will be displayed in the returned figure
    suptitle=None, # Title to be set to returned figure
    **kwargs): # fig and axs
    """A figure and set of subplots to display images of `imsize` inches."""
    if figsize is None: figsize=(ncols*imsize, nrows*imsize)
    fig, ax = plt.subplots(nrows, ncols, figsize=figsize, **kwargs)
    if suptitle is not None: fig.suptitle(suptitle)
    if nrows*ncols==1: a = array([ax])
    return fig, ax

# %% ../nbs/00_core.ipynb 81
@fc.delegates(subplots)
def get_grid(
    n, # Number of axes
    nrows=None, # Number of rows, defaulting to `int(math.sqrt(n))`
    ncols=None, # Number of columns, defaulting to `ceil(n/rows)`
    title=None, # If passed, title set to the figure
    weight='bold', # Title font weight
    size=14, # Title font size
    **kwargs): # fig and axs
    """Return a grid of `n` axes, `nrows` by `ncols`."""
    if nrows: ncols = ncols or int(np.ceil(n/nrows))
    elif ncols: nrows = nrows or int(np.ceil(n/ncols))
    else:
        nrows = int(math.sqrt(n))
        ncols = int(np.ceil(n/nrows))
    fig, axs = subplots(nrows, ncols, **kwargs)
    for i in range(n, nrows*ncols): axs.flat[i].set_axis_off()
    if title is not None: fig.suptitle(title, weight=weight, size=size)
    return fig, axs

# %% ../nbs/00_core.ipynb 82
@fc.delegates(subplots)
def show_images(
    ims:list, # Images to show
    nrows=1, # Number of rows in grid
    ncols=None, # Number of columns in grid (auto-calculated if None)
    titles=None, # Optional list of titles for each image
    noframe=True, # Hide axes, yes or no
    **kwargs):
    """Show all images `ims` as subplots with `nrows` using `titles`."""
    axs = get_grid(len(ims), **kwargs)[1].flat
    for im, t, ax in zip_longest(ims, titles or [], axs): show_image(im, ax=ax, title=t, noframe=noframe)

# %% ../nbs/00_core.ipynb 84
class Hook():
    def __init__(self, m, f): self.hook = m.register_forward_hook(partial(f, self))
    def remove(self): self.hook.remove()
    def __del__(self): self.remove()

def append_stats(hook, mod, inp, outp):
    if not hasattr(hook, 'stats'): hook.stats = ([], [])
    acts = to_cpu(outp)
    hook.stats[0].append(acts.mean())
    hook.stats[1].append(acts.std())

# %% ../nbs/00_core.ipynb 85
class Hooks(list):
    def __init__(self, ms, f): super().__init__([Hook(m, f) for m in ms])
    def __enter__(self, *args): return self
    def __exit__(self, *args): self.remove()
    def __del__(self): self.remove()
    def __delitem__(self, i):
        self[i].remove()
        super().__delitem__(i)
    def remove(self):
        for h in self: h.remove()

# %% ../nbs/00_core.ipynb 86
class HooksCallback(Callback):
    def __init__(self, hookfunc, mod_filter=fc.noop, on_train=True, on_valid=False, mods=None):
        fc.store_attr()
        super().__init__()
    
    def before_fit(self, learn):
        if self.mods: mods=self.mods
        else: mods = fc.filter_ex(learn.model.modules(), self.mod_filter)
        self.hooks = Hooks(mods, partial(self._hookfunc, learn))

    def _hookfunc(self, learn, *args, **kwargs):
        if (self.on_train and learn.training) or (self.on_valid and not learn.training): self.hookfunc(*args, **kwargs)

    def after_fit(self, learn): self.hooks.remove()
    def __iter__(self): return iter(self.hooks)
    def __len__(self): return len(self.hooks)

# %% ../nbs/00_core.ipynb 87
def append_stats(hook, mod, inp, outp):
    if not hasattr(hook, 'stats'): hook.stats = ([], [], [])
    acts = to_cpu(outp)
    hook.stats[0].append(acts.mean())
    hook.stats[1].append(acts.std())
    hook.stats[2].append(acts.abs().histc(40, 0, 10))

# %% ../nbs/00_core.ipynb 88
# Thanks to @ste for the initial version of the histogram plotting code
def get_hist(h): return torch.stack(h.stats[2]).t().float().log1p()

# %% ../nbs/00_core.ipynb 89
def get_min(h):
    h1 = torch.stack(h.stats[2]).t().float()
    return h1[:2].sum(0)/h1.sum(0)

# %% ../nbs/00_core.ipynb 90
class ActivationStats(HooksCallback):
    def __init__(self, mod_filter=fc.noop): super().__init__(append_stats, mod_filter)

    def color_dim(self, figsize=(11, 5)):
        fig, axs = get_grid(len(self), figsize=figsize)
        for ax, h in zip(axs.flat, self):
            show_image(get_hist(h), ax, origin='lower')
    
    def dead_chart(self, figsize=(11, 5)):
        fig, axs = get_grid(len(self), figsize=figsize)
        for ax, h in zip(axs.flat, self):
            ax.plot(get_min(h))
            ax.set_ylim(0.0, 1.1)

    def plot_stats(self, figsize=(10, 4)):
        fig, axs = subplots(1, 2, figsize=figsize)
        for h in self:
            for i in 0, 1: axs[i].plot(h.stats[i])
        axs[0].set_title('Means')
        axs[1].set_title('Stdevs')
        plt.legend(fc.L.range(self))

# %% ../nbs/00_core.ipynb 92
def clean_ipython_hist():
    # Code in this function mainly copied from IPython source
    if not 'get_ipython' in globals(): return
    ip = get_ipython()
    user_ns = ip.user_ns
    ip.displayhook.flush()
    pc = ip.displayhook.prompt_count + 1
    for n in range(1, pc): user_ns.pop('_i'+repr(n),None)
    user_ns.update(dict(_i='',_ii='',_iii=''))
    hm = ip.history_manager
    hm.input_hist_parsed[:] = [''] * pc
    hm.input_hist_raw[:] = [''] * pc
    hm._i = hm._ii = hm._iii = hm._i00 =  ''

# %% ../nbs/00_core.ipynb 93
def clean_tb():
    # h/t Piotr Czapla
    if hasattr(sys, 'last_traceback'):
        traceback.clear_frames(sys.last_traceback)
        delattr(sys, 'last_traceback')
    if hasattr(sys, 'last_type'): delattr(sys, 'last_type')
    if hasattr(sys, 'last_value'): delattr(sys, 'last_value')

# %% ../nbs/00_core.ipynb 94
def clean_mem():
    clean_tb()
    clean_ipython_hist()
    gc.collect()
    torch.cuda.empty_cache()

# %% ../nbs/00_core.ipynb 96
def init_weights(m, leaky=0.):
    if isinstance(m, (nn.Conv1d, nn.Conv2d, nn.Conv3d, nn.Linear)): init.kaiming_normal_(m.weight, a=leaky)

# %% ../nbs/00_core.ipynb 97
class GeneralRelu(nn.Module):
    def __init__(self, leak=None, sub=None, maxv=None):
        super().__init__()
        self.leak, self.sub, self.maxv = leak, sub, maxv

    def forward(self, x):
        x = F.leaky_relu(x, self.leak) if self.leak is not None else F.relu(x)
        if self.sub is not None: x -= self.sub
        if self.maxv is not None: x.clamp_max_(self.maxv)
        return x
