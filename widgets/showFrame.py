__author__ = 'cyrbuzz'

from base import *


class ShowFrame(QFrame):

    def __init__(self, parent=None):
        super(ShowFrame, self).__init__()
        self.parent = parent
        with open('Qss/showFrame.qss', 'r') as f:
            self.setStyleSheet(f.read())

        self.mainLayout = HBoxLayout(self)

        self.searchEngines = SearchEngines(self)
        self.engines = self.searchEngines.engines

        self.mainLayout.addWidget(self.searchEngines)

        self.searchResult = SearchResult(self)
        self.mainLayout.addWidget(self.searchResult)

    def addEngine(self, name, engine):
        self.searchEngines.addEngine(name, engine)

    def getCurrentEngine(self):

        return self.searchEngines.getCurrentEngine()

    def setText(self, text=''):
        self.searchResult.setText(text)

    def setCurrentRow(self, row):
        self.searchEngines.setCurrentRow(row)

class SearchEngines(QListWidget):

    def __init__(self, parent=None):
        super(SearchEngines, self).__init__()
        self.parent = parent
        self.engines = {}

    def addEngine(self, name, engine):
        self.engines[name] = engine

        item = QListWidgetItem(name)
        item.setTextAlignment(Qt.AlignCenter)
        self.addItem(item)

    def getCurrentEngine(self):

        return self.currentItem().text()


class SearchResult(QTextEdit):

    def __init__(self, parent=None):
        super(SearchResult, self).__init__()
        self.parent = parent
        self.setReadOnly(True)