#!/usr/bin/env python3

import os
import sys
import tkinter as tk
import apputils
import frame
import keyboard
if 'DISPLAY' in os.environ:
    import Xlib
    try:
        import pyautogui as pag
    except Xlib.error.DisplayConnectionError:
        os.system("xhost +SI:localuser:root")
else:
    import pyautogui as pag


class Application:
    """
    A class used to represent an hotkeys management application.

    ...

    Attributes
    ----------
    _hotkeys: list of tuples
        the hotkeys used by the application
    root: tkinter.Tk
        the base of the GUI
    frame: tkinter.Frame
        the frame showed by the application
    """

    def __init__(self, parent):
        self._hotkeys = apputils.read_hotkeys()
        self.root = parent
        self.root.title('MouseMove')
        self.frame = frame.GuiFrame(self, parent)
        self.frame.grid(padx=5, pady=5)
        self.root.withdraw()
        self._init_hotkeys()

    def _init_hotkeys(self):
        """
        Set hotkeys for each monitor and to use the application.
        """

        for n, monitor in enumerate(apputils.monitors):
            hotkey = '+'.join(str(i) for i in self._hotkeys[n])
            x = monitor[2] / 2 + monitor[0]
            y = monitor[3] / 2 + monitor[1]
            keyboard.add_hotkey(hotkey, pag.moveTo, args=(x, y))
        keyboard.add_hotkey('alt+shift+s', self.show)
        keyboard.add_hotkey('alt+shift+e', self.root.destroy)

    def show(self):
        """
        Shows the configuration window.
        """

        self.root.deiconify()
        self.root.update()

    def _restart(self):
        """
        Hides the configuration window and re-initialize the hotkeys.
        """

        self._hotkeys = apputils.read_hotkeys()
        keyboard.unhook_all_hotkeys()
        self._init_hotkeys()
        self.root.withdraw()

    def save(self):
        """
        Save the hotkeys configuration in a csv file.
        """

        apputils.write_hotkeys(self._hotkeys)
        self._restart()

    def get_hotkeys(self):
        """
        Returns the hotkeys.
        """

        return self._hotkeys

    def set_hotkeys(self, hotkeys):
        """
        Sets the hotkeys.
        """

        self._hotkeys = hotkeys


if os.path.sep == '/' and os.geteuid() != 0:
    sys.exit(
        """
        You need to have root privileges to run this script.
        Please try again, this time using 'sudo'. Exiting.
        """
    )
root = tk.Tk()
Application(root)
root.mainloop()
