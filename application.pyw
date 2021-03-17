#!/usr/bin/env python3

import os
import sys
import tkinter as tk
import apputils
import frame
import keyboard
import mouse


class Application:
    """
    A class used to represent an hotkeys management application.

    ...

    Attributes
    ----------
    _hotkeys: list of tuples
        the hotkeys used by the application
    _settings_hotkeys: list of tuples
        the settings hotkeys used by the application
    _root: tkinter.Tk
        the base of the GUI
    _frame: tkinter.Frame
        the frame showed by the application
    """

    def __init__(self, parent):
        self._hotkeys = apputils.read_hotkeys()
        self._settings_hotkeys = apputils.read_settings_hotkeys()
        self._root = parent
        self._root.title('MouseMove')
        self._frame = frame.GuiFrame(self, parent)
        self._frame.grid(padx=5, pady=5)
        self._root.withdraw()
        self._init_hotkeys()

    def _init_hotkeys(self):
        """
        Set hotkeys for each monitor and to use the application.
        """

        for n, monitor in enumerate(apputils.monitors):
            hotkey = '+'.join(i for i in self._hotkeys[n])
            x = monitor[2] / 2 + monitor[0]
            y = monitor[3] / 2 + monitor[1]
            keyboard.add_hotkey(hotkey, mouse.move, args=(x, y))
        keyboard.add_hotkey(
            '+'.join(i for i in self._settings_hotkeys[0]), self.show)
        keyboard.add_hotkey(
            '+'.join(i for i in self._settings_hotkeys[1]), self._root.destroy)

    def show(self):
        """
        Shows the configuration window.
        """

        self._frame.restart()
        self._root.deiconify()
        self._root.update()

    def _restart(self):
        """
        Hides the configuration window and re-initialize the hotkeys.
        """

        self._hotkeys = apputils.read_hotkeys()
        self._settings_hotkeys = apputils.read_settings_hotkeys()
        keyboard.unhook_all_hotkeys()
        self._init_hotkeys()
        self._root.withdraw()

    def save(self):
        """
        Save the hotkeys configuration in a csv file.
        """

        apputils.write_hotkeys(self._hotkeys, self._settings_hotkeys)
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

    def get_settings_hotkeys(self):
        """
        Sets the hotkeys.
        """

        return self._settings_hotkeys

    def set_settings_hotkeys(self, hotkeys):
        """
        Sets the hotkeys.
        """

        self._settings_hotkeys = hotkeys


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
