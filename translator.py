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
from slideShow import SlideShow, SlideFrame

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
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.resize(540, 490)
        
        self.searchThread = RequestThread(self)
        self.searchThread.finished.connect(self.searchResult)

        self.mainLayout = VBoxLayout(self)
        
        self.setSearchFrame()
        self.setShowFrame()


    def setSearchFrame(self):
        self.searchFrame = SearchAndControlFrame(self)
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


    def closeEvent(self, event):
        sys.exit('close')


class SearchAndControlFrame(QFrame):
    """搜索区域以及控制区域。"""
    def __init__(self, parent=None):
        super(SearchAndControlFrame, self).__init__()
        self.parent = parent
        self.mainLayout = VBoxLayout(self)

        self.controlFrame = ControlFrame(self.parent)
        self.controlFrame.setButtonSlows(self.parent.showMinimized, self.parent.close)
        self.controlFrame.setStyleFile('Qss/controlFrame.qss')

        self.searchLine = SearchFrame(self.parent)

        self.mainLayout.addWidget(self.controlFrame)
        self.mainLayout.addWidget(self.searchLine)

    def setSearchButtonConnect(self, func):
        self.searchLine.setSearchButtonConnect(func)        


    def setDisconnect(self):

        self.searchLine.setDisconnect()

    def getText(self):

        return self.searchLine.getText()

class SlideWindow(SlideShow):
    def __init__(self, parent=None):
        super(SlideWindow, self).__init__(parent)
        
        self.setWindowTitle("Definition")
        self.setWindowFlags(Qt.FramelessWindowHint)

        with open('Qss/slideWindow.qss', 'r') as f:

            self.setStyleSheet(f.read())


        self.setMinimumWidth(400)

        self.engines = {}

        self.addTab(SlideFrame(), "Shanbay", ShanbaySearch())
        
        self.slideThread = ListenThread(self)

        self.slideSearchThread = RequestThread(self)
        self.slideSearchThread.finished.connect(self.slideSearchFinished)
        
        self.slideThread.start()

    def addTab(self, widget, name, engine):
        super(SlideWindow, self).addTab(widget, name)
        self.engines[name] = engine

    def slideSearch(self, words):
        self.slideSearchThread.setTarget(self.engines[
            self.indexNames[self.getCurrentIndex()]].searchWord)
        self.slideSearchThread.setArgs(words)
        self.slideSearchThread.start()

    def slideSearchFinished(self):
        self.getCurrentWidget().setText(self.slideThread.text, self.slideSearchThread.result['definition'])
        
        if not self.isVisible():
            self.open()
            
        x, y = self.slideThread.getXY()
        self.activateWindow()
        self.move(x, y+20)


class ListenThread(ListenMouseThread):

    def __init__(self, parent=None):
        super(ListenThread, self).__init__(parent)
        self.parent = parent

        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.onClipboardChanged)
        self.data = self.clipboard.mimeData().text()

    def onClipboardChanged(self):
        super(ListenThread, self).onClipboardChanged()
        self.parent.slideSearch(self.text)

    def getXY(self):
        return self.xAndY


if __name__ == '__main__':
    app = QApplication(sys.argv)

    slideWindow = SlideWindow()

    # slideWindow.show()
    main = Window()
    main.show()


    sys.exit(app.exec_())
