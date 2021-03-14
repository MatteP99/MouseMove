#!/usr/bin/env python3

from system_hotkey import SystemHotkey
import pyautogui as pag
import tkinter as tk
import screeninfo
import apputils
import frame
import sys


class Application():
    """
    A class used to represent an hotkeys management application.

    ...

    Attributes
    ----------
    monitors : list of tuples of int
        the monitors parameters needed to the application
    hotkeys: list of tuples
        the hotkeys used by the application
    prev_hotkeys: list of tuples
        used to unbind the previous hotkeys
    root: tkinter.Tk
        the base of the GUI
    frame: tkinter.Frame
        the frame showed by the application
    """

    def __init__(self, parent):
        self.monitors = [
            (m.x, m.y, m.width, m.height) for m in screeninfo.get_monitors()
        ]
        self.hotkeys = []
        self.hk = SystemHotkey()
        self.hkp = SystemHotkey(consumer=self.moveMouse)
        apputils.readHotkeys(self.hotkeys)
        self.prev_hotkeys = self.hotkeys.copy()
        self.root = parent
        self.root.title('MouseMove')
        self.frame = frame.guiFrame(self.monitors, self.hotkeys, self, parent)
        self.frame.grid(padx=5, pady=5)
        self.root.withdraw()
        self.hk.register(('alt', 'shift', 's'), callback=lambda _: self.show())
        self.hk.register(
            ('alt', 'shift', 'e'), callback=lambda _: self.root.destroy())
        self._initHotkeys()

    def moveMouse(self, event, hotkey, args):
        """
        Default callback to move the mouse.
        """
    
        pag.moveTo(args[0][0], args[0][1])

    def _initHotkeys(self):
        """
        Set hotkeys for each monitor and to use the application.
        """

        for n, monitor in enumerate(self.monitors):
            hotkey = self.hotkeys[n]
            x = monitor[2] / 2 + monitor[0]
            y = monitor[3] / 2 + monitor[1]
            self.hkp.register(hotkey, x, y)

    def show(self):
        """
        Shows the configuration window.
        """

        self.root.deiconify()
        self.root.update()

    def _restart(self):
        """
        Hides the configuration window and re-intialize the hotkeys.
        """
        
        for hotkey in self.prev_hotkeys:
            self.hkp.unregister(hotkey)
        self.hotkeys.clear()
        apputils.readHotkeys(self.hotkeys)
        self.prev_hotkeys = self.hotkeys.copy()
        self._initHotkeys()
        self.root.withdraw()

    def _save(self):
        """
        Save the hotkeys configuration in a csv file.
        """

        self.hotkeys[self.frame.prevCombo] = (self.frame.hotkeyEntry.get().split('+'))
        apputils.writeHotkeys(self.hotkeys)
        self._restart()


root = tk.Tk()
Application(root)
root.mainloop()
