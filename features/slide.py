__author__ = 'cyrbuzz'
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication
from pywinauto.win32_hooks import Hook, KeyboardEvent, MouseEvent

import keyboard
import win32api

"""
提供划词线程。


思路是，获取当前鼠标按下的消息，进入判断，当鼠标放开时，
按键ctrl+c进行复制，若剪切板与之前不同则获取词汇。
"""

class ListenMouseThread(QThread):

    def __init__(self, parent=None):
        super(ListenMouseThread, self).__init__()
        self.parnet = parent
        # 用于检测ctrl键是否已经按下。
        # self.ctrlDown = False
        # # 
        # self.allowCopy = False
        # # sysCopy
        # self.sysCopy = False

        self.text = ''
        self.mouseX = 0
        self.mouseY = 0

        self.xAndY = []


    def run(self):
        hk = Hook()
        hk.handler = self.handleEvents
        hk.hook(keyboard=True, mouse=True)

    def onClipboardChanged(self):
        data = self.clipboard.mimeData()
        if data.hasText():
            self.text = data.text()

        # # 还原回之前的内容。    
        # if not self.allowCopy:
        #     self.clipboard.setText(self.data)
        # else:
        #     self.allowCopy = False

        # self.sysCopy = False
        
    def handleEvents(self, args):
        if isinstance(args, MouseEvent):
            if args.current_key == 'LButton' and args.event_type == 'key down':
                self.mouseX = args.mouse_x
                self.mouseY = args.mouse_y
                self.xAndY = win32api.GetCursorPos()

            if args.current_key == 'LButton' and args.event_type == 'key up':
                if self.mouseX != args.mouse_x or self.mouseY != args.mouse_y:
                    keyboard.press_and_release('ctrl+c')

        # if isinstance(args, KeyboardEvent):
        #     if 'control' in args.current_key and args.event_type == 'key down':
        #         self.ctrlDown = True
        #     if 'control' in args.current_key and args.event_type == 'key up':
        #         self.ctrlDown = False
            
        #     if args.current_key == 'C' and self.ctrlDown:
        #         if self.sysCopy:
        #             pass
        #         else:
        #             self.allowCopy = True


# down = False

# def handleEvents(args):
#     global down
#     if isinstance(args, MouseEvent):
#         if args.current_key == 'LButton' and args.event_type == 'key up':
#             keyboard.press_and_release('ctrl+c')

#     if isinstance(args, KeyboardEvent):
#         if 'control' in args.current_key and args.event_type == 'key down':
#             down = True
#         if 'control' in args.current_key and args.event_type == 'key up':
#             down = False
        
#         if args.current_key == 'C' and down:
#             print(1)

# def onClipboardChanged()
#     data = clipboard.mimeData()
#     if data.hasText():
#         print(data.text())

# app = QApplication([])
# clipboard = app.clipboard()
# clipboard.dataChanged.connect(onClipboardChanged)

if __name__ == '__main__':
    print('no config.')
    hk = Hook()
    hk.handler = handleEvents
    hk.hook(keyboard=True, mouse=True)
