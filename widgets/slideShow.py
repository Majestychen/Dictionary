__author__ = 'cyrbuzz'

from base import *

"""
划词的显示界面。
"""

class SlideShow(QDialog):

    def __init__(self, parent=None):
        super(SlideShow, self).__init__()
        self.setObjectName("slideShow")
        self.parent = parent
        
        self.indexNames = []

        self.mainLayout = VBoxLayout(self)

        self.tab = QTabWidget()
        self.tab.setObjectName("slideTab")

        self.mainLayout.addWidget(self.tab)

    def addTab(self, widget, name=""):
        self.tab.addTab(widget, name)
        self.indexNames.append(name)

    def getCurrentIndex(self):
        return self.tab.currentIndex()

    def getCurrentWidget(self):
        return self.tab.currentWidget()

class SlideFrame(QFrame):

    def __init__(self, parent=None):
        super(SlideFrame, self).__init__()
        self.parent = parent

        self.mainLayout = VBoxLayout(self)

        self.wordLabel = QLabel("")
        self.mainLayout.addWidget(self.wordLabel)

        self.wordDefinitionLabel = QLabel("Test2")
        self.mainLayout.addWidget(self.wordDefinitionLabel)

    def setText(self, word, wordDefinition):
        # self.wordLabel.setText(word)
        self.wordDefinitionLabel.setText("<b>{0}</b>".format(wordDefinition.replace('\n', '<br>')))

