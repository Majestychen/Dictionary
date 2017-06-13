__author__ = 'cyrbuzz'

from base import *


class SearchFrame(QFrame):

    def __init__(self, parent=None):
        super(SearchFrame, self).__init__()
        self.setObjectName("searchFrame")
        self.setMaximumHeight(245)
        self.parent = parent
        with open('Qss/searchFrame.qss', 'r') as f:
            self.setStyleSheet(f.read())

        self.mainLayout = VBoxLayout(self)
        self.mainLayout.addStretch(1)
        
        self.searchLine = SearchLine(self)
        self.mainLayout.addWidget(self.searchLine)

        self.mainLayout.addStretch(1)

    def setSearchButtonConnect(self, func):
        
        self.searchLine.searchButton.clicked.connect(func)

    def setDisconnect(self):

        self.searchLine.searchButton.disconnect()

    def getText(self):

        return self.searchLine.searchLine.text()


class SearchLine(QFrame):
    """包括一个输入框和一个查询按钮。"""
    def __init__(self, parent=None):
        super(SearchLine, self).__init__()
        self.setObjectName("SearchLine")
        self.parent = parent

        self.mainLayout = HBoxLayout(self)

        # 因为有汉字，要用UTF-8编码。
        with open('Qss/searchLine.qss', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

        self.mainLayout.addStretch(1)

        self.searchLine = QLineEdit()
        self.searchLine.setMinimumSize(220, 20)
        self.mainLayout.addWidget(self.searchLine)

        self.mainLayout.addSpacing(10)

        self.searchButton = QPushButton("查询")
        self.mainLayout.addWidget(self.searchButton)

        self.mainLayout.addStretch(1)
