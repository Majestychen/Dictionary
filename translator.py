__author__ = 'cyrbuzz'
import sys

sys.path.append('widgets')
sys.path.append('apis')
sys.path.append('features')

from base import *
from slide import ListenMouseThread
from shanbay import ShanbaySearch

from showFrame import ShowFrame
from searchFrame import SearchFrame

"""
主界面分成。
-------------------------
搜索框/划词选项。
-------------------------
选择搜词引擎|显示搜索结果.
-------------------------

"""


class Window(QWidget):
    """Window 承载整个界面。"""
    def __init__(self):
        super(Window, self).__init__()
        self.setObjectName('MainWindow')
        self.setWindowTitle('Dictionary')
        self.resize(540, 490)
        
        self.searchThread = RequestThread(self)
        self.searchThread.finished.connect(self.searchResult)

        self.slideThread = ListenThread(self)

        self.mainLayout = VBoxLayout(self)
        
        self.setSearchFrame()
        self.setShowFrame()

        self.slideThread.start()

    def setSearchFrame(self):
        self.searchFrame = SearchFrame(self)
        self.searchFrame.setSearchButtonConnect(self.searchWord)

        self.mainLayout.addWidget(self.searchFrame)

    def setShowFrame(self):
        self.showFrame = ShowFrame(self)
        self.mainLayout.addWidget(self.showFrame)

        self.showFrame.addEngine('Shanbay', ShanbaySearch())
        self.showFrame.setCurrentRow(0)

    def searchWord(self):
        words = self.searchFrame.getText()
        self.startSearch(words)

    def startSearch(self, words):
        self.searchThread.setTarget(self.showFrame.engines[self.showFrame.getCurrentEngine()].searchWord)
        self.searchThread.setArgs(words)
        self.searchThread.start()

    def searchResult(self):
        self.showFrame.setText(self.searchThread.result['definition'])

    def addEngine(self, name, funcName):

        self.showFrame.addEngine(name, funcName())


class ListenThread(ListenMouseThread):

    def __init__(self, parent=None):
        super(ListenThread, self).__init__(parent)
        self.parent = parent

        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.onClipboardChanged)
        self.data = self.clipboard.mimeData().text()

    def onClipboardChanged(self):
        super(ListenThread, self).onClipboardChanged()
        self.parent.startSearch(self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
