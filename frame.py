import tkinter as tk
import keyboard

import apputils


class GuiFrame(tk.Frame):
    """
    A class used to represent the gui of the application.

    ...

    Attributes
    ----------
    parent: Application
        the application that contain this frame
    """

    def __init__(self, parent, master=None):
        super().__init__(master)
        self.parent = parent
        self._create_widgets()

    def _create_widgets(self):
        """
        Creates the necessary widgets for the gui.
        """

        hotkeys = self.parent.get_hotkeys()
        values = [
            f"Monitor {n}" for n, monitor in enumerate(apputils.monitors, 1)
        ]
        self._monitorsCombo = tk.ttk.Combobox(
            self, values=values, state="readonly", width=10)
        self._monitorsCombo.grid(row=0, column=0, padx=5, pady=5)
        self._monitorsCombo.bind("<<ComboboxSelected>>", self._callback)
        self._monitorsCombo.current(0)
        self.prevCombo = self._monitorsCombo.current()
        self._label = tk.Label(self, text='+'.join(str(i) for i in hotkeys[0]))
        self._label.grid(row=0, column=1, padx=5, pady=5)
        self._read_hotkey_button = tk.Button(
            self, text='Register hotkey', command=self._read_hotkey)
        self._read_hotkey_button.grid(row=0, column=2, padx=5, pady=5, )
        self._saveButton = tk.Button(
            self, text='Save and quit', command=self.parent.save)
        self._saveButton.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

    def _callback(self, args):
        """
        The callback used to track the changes to the combobox.
        """

        hotkeys = self.parent.get_hotkeys()
        self._label.config(
            text=str('+'.join(
                str(i) for i in hotkeys[self._monitorsCombo.current()])))

    def _read_hotkey(self):
        """
        Callback used to get the hotkey pressed by the user.
        """

        hotkeys = self.parent.get_hotkeys()
        hotkeys[self._monitorsCombo.current()] = \
            keyboard.read_hotkey(suppress=False).split("+")
        self._label.config(
            text=str('+'.join(
                str(i) for i in hotkeys[self._monitorsCombo.current()])))
        self.parent.set_hotkeys(hotkeys)
