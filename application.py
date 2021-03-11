import pyautogui as pag
import tkinter as tk
import screeninfo
import keyboard
import apputils
import gui


class Application():

    def __init__(self, parent):
        self.monitors = [(m.x, m.y, m.width, m.height) for m in screeninfo.get_monitors()]
        self.hotkeys = []
        apputils.readHotkeys(self.hotkeys)
        self.root = parent
        self.root.title('MouseMove')
        self.frame = gui.guiFrame(self.monitors, self.hotkeys, self, parent)
        self.frame.grid(padx=5, pady=5)
        self.root.withdraw()
        self.frame.createWidgets()
        self.initHotkeys()

    def initHotkeys(self):
        for n, monitor in enumerate(self.monitors):
            hotkey = f'{self.hotkeys[n][0]}'
            x = monitor[2] / 2 + monitor[0]
            y = monitor[3] / 2 + monitor[1]
            keyboard.add_hotkey(hotkey, pag.moveTo, args=(x, y))
        keyboard.add_hotkey('alt+shift+s', self.show)
        keyboard.add_hotkey('alt+shift+0', self.root.destroy)

    def show(self):
        self.root.deiconify()
        self.root.update()

    def restart(self):
        apputils.readHotkeys(self.hotkeys)
        keyboard.unhook_all_hotkeys()
        self.initHotkeys()
        self.root.withdraw()

    def save(self):
        self.hotkeys[self.frame.prevCombo][0] = self.frame.hotkeyEntry.get()
        apputils.writeHotkeys(self.hotkeys)
        self.restart()


root = tk.Tk()
Application(root)
root.mainloop()
