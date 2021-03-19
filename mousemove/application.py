import copy
import tkinter as tk
import keyboard as kb
import mouse
from mousemove import apputils, frame


class Application(tk.Tk):
    """
    A class used to represent an hotkeys management application.

    ...

    Attributes
    ----------
    _hotkeys: list of tuples
        the hotkeys used by the application
    _frame: tkinter.Frame
        the gui showed by the application
    """

    def __init__(self):
        super().__init__()
        self._hotkeys = apputils.read_hotkeys()
        self.title('MouseMove')
        self._frame = frame.GuiFrame(self)
        self._frame.grid(padx=5, pady=5)
        self.withdraw()
        self._init_hotkeys()

    def _init_hotkeys(self):
        """
        Set hotkeys for each monitor and to use the application.
        """

        for n, monitor in enumerate(apputils.monitors):
            hotkey = '+'.join(i for i in self._hotkeys[n])
            x = monitor[2] / 2 + monitor[0]
            y = monitor[3] / 2 + monitor[1]
            kb.add_hotkey(hotkey, mouse.move, args=(x, y))

        kb.add_hotkey(kb.get_hotkey_name(self._hotkeys[-2]), self.show)
        kb.add_hotkey(kb.get_hotkey_name(self._hotkeys[-1]), self.destroy)

    def show(self, unhook=True):
        """
        Removes all the hotkeys (by default) and shows the configuration window.
        """

        if unhook:
            kb.unhook_all_hotkeys()
            self._frame.restart()
        self.deiconify()
        self.update()

    def save_and_restart(self):
        """
        Save the hotkeys configuration and restart the program.
        """

        apputils.write_hotkeys(self._hotkeys)
        self._hotkeys = apputils.read_hotkeys()
        self._init_hotkeys()
        self.withdraw()

    def get_hotkeys(self):
        """
        Returns the hotkeys.
        """

        return copy.deepcopy(self._hotkeys)

    def set_hotkeys(self, hotkeys):
        """
        Sets the hotkeys.
        """

        if isinstance(hotkeys, list) and \
                all((isinstance(hotkey, list) for hotkey in hotkeys)):
            self._hotkeys = hotkeys
        else:
            raise ValueError
