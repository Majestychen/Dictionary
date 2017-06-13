__author__ = 'cyrbuzz'

"""
用于定义一些基本的组件，慢慢增加。
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class VBoxLayout(QVBoxLayout):

    def __init__(self, *args):
        super(VBoxLayout, self).__init__(*args)

        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)


class HBoxLayout(QHBoxLayout):

    def __init__(self, *args):
        super(HBoxLayout, self).__init__(*args)

        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)


class RequestThread(QThread):
    """异步请求，类似Pyhton封装的Thread形式，用QThread在简单封装一下。"""
    def __init__(self, parent=None, target=None, *args, **kwargs):
        super(RequestThread, self).__init__()

        self.parent = parent
        self.args = args
        self.kwargs = kwargs
        self.target = target
        self.result = 0

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def setTarget(self, target=None):
        """方便多次调用。"""
        self.target = target

    def setArgs(self, *args, **kwargs):
        """方便多次调用。"""
        self.args = args
        self.kwargs = kwargs
