import keyboard
import apputils
import tkinter as tk
from tkinter import ttk


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

    @staticmethod
    def _hotkey_text(val):
        """
        Returns the processed text to be displayed
        """

        return keyboard.normalize_name('+'.join(i for i in val))

    def _create_widgets(self):
        """
        Creates the necessary widgets for the gui.
        """

        hotkeys = self.parent.get_hotkeys()
        values = [
            f"Monitor {n}" for n, _ in enumerate(apputils.monitors, 1)
        ]
        values.append("Open settings")
        values.append("Quit program")

        self.__monitorsCombo = ttk.Combobox(
            self, values=values, state="readonly", width=13)
        self.__monitorsCombo.grid(row=0, column=0, padx=5, pady=5)
        self.__monitorsCombo.bind("<<ComboboxSelected>>", self._callback)
        self.__monitorsCombo.current(0)

        self.__label = tk.Label(self, text=self._hotkey_text(hotkeys[0]))
        self.__label.grid(row=0, column=1, padx=5, pady=5)

        self.__read_hotkey_button = tk.Button(
            self, text='Register hotkey', command=self._read_hotkey)
        self.__read_hotkey_button.grid(row=0, column=2, padx=5, pady=5, )

        self._saveButton = tk.Button(
            self, text='Save and quit', command=self.parent.save)
        self._saveButton.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

    def _callback(self, args):
        """
        The callback used to track the changes to the combobox.
        """

        hotkeys = self.parent.get_hotkeys()
        txt = self._hotkey_text(hotkeys[self.__monitorsCombo.current()])
        self.__label.config(text=txt)

    def _read_hotkey(self):
        """
        Callback used to get the hotkey pressed by the user.
        """

        hotkeys = self.parent.get_hotkeys()
        hotkeys[self.__monitorsCombo.current()] = \
            keyboard.read_hotkey(suppress=False).split("+")
        self.parent.set_hotkeys(hotkeys)
        txt = self._hotkey_text(hotkeys[self.__monitorsCombo.current()])
        self.__label.config(text=txt)

    def restart(self):
        """
        Resets the frame.
        """
        hotkeys = self.parent.get_hotkeys()
        self.__monitorsCombo.current(0)
        self.__label.config(text=self._hotkey_text(hotkeys[0]))
