# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/atai',
                'doc_host': 'https://frenio.github.io',
                'git_url': 'https://github.com/frenio/atai',
                'lib_path': 'atai'},
  'syms': { 'atai.core': { 'atai.core.ActivationStats': ('core.html#activationstats', 'atai/core.py'),
                           'atai.core.ActivationStats.__init__': ('core.html#activationstats.__init__', 'atai/core.py'),
                           'atai.core.ActivationStats.color_dim': ('core.html#activationstats.color_dim', 'atai/core.py'),
                           'atai.core.ActivationStats.dead_chart': ('core.html#activationstats.dead_chart', 'atai/core.py'),
                           'atai.core.ActivationStats.plot_stats': ('core.html#activationstats.plot_stats', 'atai/core.py'),
                           'atai.core.BaseSchedCB': ('core.html#baseschedcb', 'atai/core.py'),
                           'atai.core.BaseSchedCB.__init__': ('core.html#baseschedcb.__init__', 'atai/core.py'),
                           'atai.core.BaseSchedCB.before_fit': ('core.html#baseschedcb.before_fit', 'atai/core.py'),
                           'atai.core.BaseSchedCB.step': ('core.html#baseschedcb.step', 'atai/core.py'),
                           'atai.core.BatchSchedCB': ('core.html#batchschedcb', 'atai/core.py'),
                           'atai.core.BatchSchedCB.after_batch': ('core.html#batchschedcb.after_batch', 'atai/core.py'),
                           'atai.core.Block': ('core.html#block', 'atai/core.py'),
                           'atai.core.Block.__init__': ('core.html#block.__init__', 'atai/core.py'),
                           'atai.core.Block.forward': ('core.html#block.forward', 'atai/core.py'),
                           'atai.core.Callback': ('core.html#callback', 'atai/core.py'),
                           'atai.core.CancelBatchException': ('core.html#cancelbatchexception', 'atai/core.py'),
                           'atai.core.CancelEpochException': ('core.html#cancelepochexception', 'atai/core.py'),
                           'atai.core.CancelFitException': ('core.html#cancelfitexception', 'atai/core.py'),
                           'atai.core.DataLoaders': ('core.html#dataloaders', 'atai/core.py'),
                           'atai.core.DataLoaders.__init__': ('core.html#dataloaders.__init__', 'atai/core.py'),
                           'atai.core.Dataset': ('core.html#dataset', 'atai/core.py'),
                           'atai.core.Dataset.__getitem__': ('core.html#dataset.__getitem__', 'atai/core.py'),
                           'atai.core.Dataset.__init__': ('core.html#dataset.__init__', 'atai/core.py'),
                           'atai.core.Dataset.__len__': ('core.html#dataset.__len__', 'atai/core.py'),
                           'atai.core.DeviceCB': ('core.html#devicecb', 'atai/core.py'),
                           'atai.core.DeviceCB.__init__': ('core.html#devicecb.__init__', 'atai/core.py'),
                           'atai.core.DeviceCB.before_batch': ('core.html#devicecb.before_batch', 'atai/core.py'),
                           'atai.core.DeviceCB.before_fit': ('core.html#devicecb.before_fit', 'atai/core.py'),
                           'atai.core.EpochSchedCB': ('core.html#epochschedcb', 'atai/core.py'),
                           'atai.core.EpochSchedCB.after_epoch': ('core.html#epochschedcb.after_epoch', 'atai/core.py'),
                           'atai.core.FeedForward': ('core.html#feedforward', 'atai/core.py'),
                           'atai.core.FeedForward.__init__': ('core.html#feedforward.__init__', 'atai/core.py'),
                           'atai.core.FeedForward.forward': ('core.html#feedforward.forward', 'atai/core.py'),
                           'atai.core.GeneralRelu': ('core.html#generalrelu', 'atai/core.py'),
                           'atai.core.GeneralRelu.__init__': ('core.html#generalrelu.__init__', 'atai/core.py'),
                           'atai.core.GeneralRelu.forward': ('core.html#generalrelu.forward', 'atai/core.py'),
                           'atai.core.Head': ('core.html#head', 'atai/core.py'),
                           'atai.core.Head.__init__': ('core.html#head.__init__', 'atai/core.py'),
                           'atai.core.Head.forward': ('core.html#head.forward', 'atai/core.py'),
                           'atai.core.Hook': ('core.html#hook', 'atai/core.py'),
                           'atai.core.Hook.__del__': ('core.html#hook.__del__', 'atai/core.py'),
                           'atai.core.Hook.__init__': ('core.html#hook.__init__', 'atai/core.py'),
                           'atai.core.Hook.remove': ('core.html#hook.remove', 'atai/core.py'),
                           'atai.core.Hooks': ('core.html#hooks', 'atai/core.py'),
                           'atai.core.Hooks.__del__': ('core.html#hooks.__del__', 'atai/core.py'),
                           'atai.core.Hooks.__delitem__': ('core.html#hooks.__delitem__', 'atai/core.py'),
                           'atai.core.Hooks.__enter__': ('core.html#hooks.__enter__', 'atai/core.py'),
                           'atai.core.Hooks.__exit__': ('core.html#hooks.__exit__', 'atai/core.py'),
                           'atai.core.Hooks.__init__': ('core.html#hooks.__init__', 'atai/core.py'),
                           'atai.core.Hooks.remove': ('core.html#hooks.remove', 'atai/core.py'),
                           'atai.core.HooksCallback': ('core.html#hookscallback', 'atai/core.py'),
                           'atai.core.HooksCallback.__init__': ('core.html#hookscallback.__init__', 'atai/core.py'),
                           'atai.core.HooksCallback.__iter__': ('core.html#hookscallback.__iter__', 'atai/core.py'),
                           'atai.core.HooksCallback.__len__': ('core.html#hookscallback.__len__', 'atai/core.py'),
                           'atai.core.HooksCallback._hookfunc': ('core.html#hookscallback._hookfunc', 'atai/core.py'),
                           'atai.core.HooksCallback.after_fit': ('core.html#hookscallback.after_fit', 'atai/core.py'),
                           'atai.core.HooksCallback.before_fit': ('core.html#hookscallback.before_fit', 'atai/core.py'),
                           'atai.core.LRFinderCB': ('core.html#lrfindercb', 'atai/core.py'),
                           'atai.core.LRFinderCB.__init__': ('core.html#lrfindercb.__init__', 'atai/core.py'),
                           'atai.core.LRFinderCB.after_batch': ('core.html#lrfindercb.after_batch', 'atai/core.py'),
                           'atai.core.LRFinderCB.before_fit': ('core.html#lrfindercb.before_fit', 'atai/core.py'),
                           'atai.core.LRFinderCB.cleanup_fit': ('core.html#lrfindercb.cleanup_fit', 'atai/core.py'),
                           'atai.core.Learner': ('core.html#learner', 'atai/core.py'),
                           'atai.core.Learner.__getattr__': ('core.html#learner.__getattr__', 'atai/core.py'),
                           'atai.core.Learner.__init__': ('core.html#learner.__init__', 'atai/core.py'),
                           'atai.core.Learner._fit': ('core.html#learner._fit', 'atai/core.py'),
                           'atai.core.Learner._one_batch': ('core.html#learner._one_batch', 'atai/core.py'),
                           'atai.core.Learner._one_epoch': ('core.html#learner._one_epoch', 'atai/core.py'),
                           'atai.core.Learner.callback': ('core.html#learner.callback', 'atai/core.py'),
                           'atai.core.Learner.fit': ('core.html#learner.fit', 'atai/core.py'),
                           'atai.core.Learner.one_epoch': ('core.html#learner.one_epoch', 'atai/core.py'),
                           'atai.core.Learner.training': ('core.html#learner.training', 'atai/core.py'),
                           'atai.core.MetricsCB': ('core.html#metricscb', 'atai/core.py'),
                           'atai.core.MetricsCB.__init__': ('core.html#metricscb.__init__', 'atai/core.py'),
                           'atai.core.MetricsCB._log': ('core.html#metricscb._log', 'atai/core.py'),
                           'atai.core.MetricsCB.after_batch': ('core.html#metricscb.after_batch', 'atai/core.py'),
                           'atai.core.MetricsCB.after_epoch': ('core.html#metricscb.after_epoch', 'atai/core.py'),
                           'atai.core.MetricsCB.before_epoch': ('core.html#metricscb.before_epoch', 'atai/core.py'),
                           'atai.core.MetricsCB.before_fit': ('core.html#metricscb.before_fit', 'atai/core.py'),
                           'atai.core.MultiHeadAttention': ('core.html#multiheadattention', 'atai/core.py'),
                           'atai.core.MultiHeadAttention.__init__': ('core.html#multiheadattention.__init__', 'atai/core.py'),
                           'atai.core.MultiHeadAttention.forward': ('core.html#multiheadattention.forward', 'atai/core.py'),
                           'atai.core.ProgressCB': ('core.html#progresscb', 'atai/core.py'),
                           'atai.core.ProgressCB.__init__': ('core.html#progresscb.__init__', 'atai/core.py'),
                           'atai.core.ProgressCB._log': ('core.html#progresscb._log', 'atai/core.py'),
                           'atai.core.ProgressCB.after_batch': ('core.html#progresscb.after_batch', 'atai/core.py'),
                           'atai.core.ProgressCB.after_epoch': ('core.html#progresscb.after_epoch', 'atai/core.py'),
                           'atai.core.ProgressCB.before_epoch': ('core.html#progresscb.before_epoch', 'atai/core.py'),
                           'atai.core.ProgressCB.before_fit': ('core.html#progresscb.before_fit', 'atai/core.py'),
                           'atai.core.RecorderCB': ('core.html#recordercb', 'atai/core.py'),
                           'atai.core.RecorderCB.__init__': ('core.html#recordercb.__init__', 'atai/core.py'),
                           'atai.core.RecorderCB.after_batch': ('core.html#recordercb.after_batch', 'atai/core.py'),
                           'atai.core.RecorderCB.before_fit': ('core.html#recordercb.before_fit', 'atai/core.py'),
                           'atai.core.RecorderCB.plot': ('core.html#recordercb.plot', 'atai/core.py'),
                           'atai.core.ResBlock1d': ('core.html#resblock1d', 'atai/core.py'),
                           'atai.core.ResBlock1d.__init__': ('core.html#resblock1d.__init__', 'atai/core.py'),
                           'atai.core.ResBlock1d.forward': ('core.html#resblock1d.forward', 'atai/core.py'),
                           'atai.core.Reshape': ('core.html#reshape', 'atai/core.py'),
                           'atai.core.Reshape.forward': ('core.html#reshape.forward', 'atai/core.py'),
                           'atai.core.SingleBatchCB': ('core.html#singlebatchcb', 'atai/core.py'),
                           'atai.core.SingleBatchCB.after_batch': ('core.html#singlebatchcb.after_batch', 'atai/core.py'),
                           'atai.core.TrainCB': ('core.html#traincb', 'atai/core.py'),
                           'atai.core.TrainCB.__init__': ('core.html#traincb.__init__', 'atai/core.py'),
                           'atai.core.TrainCB.backward': ('core.html#traincb.backward', 'atai/core.py'),
                           'atai.core.TrainCB.get_loss': ('core.html#traincb.get_loss', 'atai/core.py'),
                           'atai.core.TrainCB.predict': ('core.html#traincb.predict', 'atai/core.py'),
                           'atai.core.TrainCB.step': ('core.html#traincb.step', 'atai/core.py'),
                           'atai.core.TrainCB.zero_grad': ('core.html#traincb.zero_grad', 'atai/core.py'),
                           'atai.core.TrainLearner': ('core.html#trainlearner', 'atai/core.py'),
                           'atai.core.TrainLearner.backward': ('core.html#trainlearner.backward', 'atai/core.py'),
                           'atai.core.TrainLearner.get_loss': ('core.html#trainlearner.get_loss', 'atai/core.py'),
                           'atai.core.TrainLearner.predict': ('core.html#trainlearner.predict', 'atai/core.py'),
                           'atai.core.TrainLearner.step': ('core.html#trainlearner.step', 'atai/core.py'),
                           'atai.core.TrainLearner.zero_grad': ('core.html#trainlearner.zero_grad', 'atai/core.py'),
                           'atai.core.TransformerModel': ('core.html#transformermodel', 'atai/core.py'),
                           'atai.core.TransformerModel.__init__': ('core.html#transformermodel.__init__', 'atai/core.py'),
                           'atai.core.TransformerModel.forward': ('core.html#transformermodel.forward', 'atai/core.py'),
                           'atai.core._beta1': ('core.html#_beta1', 'atai/core.py'),
                           'atai.core._beta2': ('core.html#_beta2', 'atai/core.py'),
                           'atai.core._conv1d_block': ('core.html#_conv1d_block', 'atai/core.py'),
                           'atai.core._lr': ('core.html#_lr', 'atai/core.py'),
                           'atai.core.append_stats': ('core.html#append_stats', 'atai/core.py'),
                           'atai.core.clean_ipython_hist': ('core.html#clean_ipython_hist', 'atai/core.py'),
                           'atai.core.clean_mem': ('core.html#clean_mem', 'atai/core.py'),
                           'atai.core.clean_tb': ('core.html#clean_tb', 'atai/core.py'),
                           'atai.core.conv1d': ('core.html#conv1d', 'atai/core.py'),
                           'atai.core.get_dls': ('core.html#get_dls', 'atai/core.py'),
                           'atai.core.get_grid': ('core.html#get_grid', 'atai/core.py'),
                           'atai.core.get_hist': ('core.html#get_hist', 'atai/core.py'),
                           'atai.core.get_min': ('core.html#get_min', 'atai/core.py'),
                           'atai.core.init_weights': ('core.html#init_weights', 'atai/core.py'),
                           'atai.core.lr_find': ('core.html#lr_find', 'atai/core.py'),
                           'atai.core.run_cbs': ('core.html#run_cbs', 'atai/core.py'),
                           'atai.core.show_image': ('core.html#show_image', 'atai/core.py'),
                           'atai.core.show_images': ('core.html#show_images', 'atai/core.py'),
                           'atai.core.subplots': ('core.html#subplots', 'atai/core.py'),
                           'atai.core.to_cpu': ('core.html#to_cpu', 'atai/core.py'),
                           'atai.core.to_device': ('core.html#to_device', 'atai/core.py'),
                           'atai.core.with_cbs': ('core.html#with_cbs', 'atai/core.py'),
                           'atai.core.with_cbs.__call__': ('core.html#with_cbs.__call__', 'atai/core.py'),
                           'atai.core.with_cbs.__init__': ('core.html#with_cbs.__init__', 'atai/core.py')}}}
