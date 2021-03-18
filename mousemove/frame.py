import tkinter as tk
from tkinter import ttk
import keyboard
from mousemove import apputils


class GuiFrame(tk.Frame):
    """
    A class used to represent the gui of the application.

    ...

    Attributes
    ----------
    __monitors_combo: ttk.Combobox
         comboBox that contains the values of the monitors and the settings
    __label: tk.Label
        label displaying the hotkey for the current value of the combobox
    __read_hotkey_button: tk.Button
        button used to trigger the hotkey reading function
    __save_button: tk.Button
        button used to save and close the settings window

    """

    def __init__(self, master=None):
        super().__init__(master)
        self.__monitors_combo = ttk.Combobox(self, state="readonly", width=13)
        self.__label = tk.Label(self)
        self.__read_hotkey_button = tk.Button(
            self, text='Register hotkey', command=self._read_hotkey)
        self.__save_button = tk.Button(
            self, text='Save and quit', command=self.master.save)
        self._start_widgets()

    @staticmethod
    def _hk_txt(hotkey_text):
        """
        Returns the processed text for the hotkey to be displayed
        """

        return keyboard.normalize_name('+'.join(i for i in hotkey_text))

    def _start_widgets(self):
        """
        Sets the necessary widgets for the gui.
        """

        hotkeys = self.master.get_hotkeys()
        values = [
            f"Monitor {n}" for n, _ in enumerate(apputils.monitors, 1)
        ]
        values.append("Open settings")
        values.append("Quit program")

        self.__monitors_combo.config(values=values)
        self.__monitors_combo.grid(row=0, column=0, padx=5, pady=5)
        self.__monitors_combo.bind("<<ComboboxSelected>>", self._callback)
        self.__monitors_combo.current(0)
        self.__label.config(text=self._hk_txt(hotkeys[0]))
        self.__label.grid(row=0, column=1, padx=5, pady=5)
        self.__read_hotkey_button.grid(row=0, column=2, padx=5, pady=5, )
        self.__save_button.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

    def _callback(self, args):
        """
        The callback used to track the changes to the combobox.
        """

        hotkeys = self.master.get_hotkeys()
        txt = self._hk_txt(hotkeys[self.__monitors_combo.current()])
        self.__label.config(text=txt)

    def _read_hotkey(self):
        """
        Callback used to get the hotkey pressed by the user.
        """

        hotkeys = self.master.get_hotkeys()
        hotkeys[self.__monitors_combo.current()] = \
            keyboard.read_hotkey(suppress=False).split("+")
        self.master.set_hotkeys(hotkeys)
        txt = self._hk_txt(hotkeys[self.__monitors_combo.current()])
        self.__label.config(text=txt)

    def restart(self):
        """
        Resets the frame.
        """
        hotkeys = self.master.get_hotkeys()
        self.__monitors_combo.current(0)
        self.__label.config(text=self._hk_txt(hotkeys[0]))
