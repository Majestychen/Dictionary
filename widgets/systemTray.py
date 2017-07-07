from base import *

class SystemTray(QSystemTrayIcon):

    def __init__(self, parent=None, iconPath=None):
        super(SystemTray, self).__init__(QIcon(iconPath))
        self.parent = parent

        self.menu = QMenu(self.parent)
        self.setContextMenu(self.menu)

    def addAction(self, action):
        self.menu.addAction(action)

    def __del__(self):
        self.hide()