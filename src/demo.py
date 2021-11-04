from __future__ import absolute_import
#_future_ 这个指令就是将行为切换成为绝对导入，因为使用绝对导入的话会变成默认设置。
from __future__ import division 
from __future__ import print_function

import _init_paths
#在这里会看到导入了一个init_paths 文件

import logging
import os
import os.path as osp
from opts import opts
#opts没有找到
from tracking_utils.utils import mkdir_if_missing
#

