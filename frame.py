import tkinter as tk


class guiFrame(tk.Frame):
    """
    A class used to represent the gui of the application.

    ...

    Attributes
    ----------
    monitors : list of tuples of int
        the monitors parameters needed to the application
    hotkeys: list of tuples
        the hotkeys used by the application
    parent: Application
        the application that contain this frame
    """

    def __init__(self, monitors, hotkeys, parent, master=None):
        super().__init__(master)
        self.monitors = monitors
        self.hotkeys = hotkeys
        self.parent = parent
        self._createWidgets()

    def _createWidgets(self):
        """
        Creates the necessary widgets for the gui.
        """
    
        vals = [f"Monitor {n+1}" for n, monitor in enumerate(self.monitors)]
        self.monitorsCombo = tk.ttk.Combobox(
            self, values=vals, state="readonly")
        self.monitorsCombo.grid(row=0, column=0, padx=5, pady=5)
        self.monitorsCombo.bind("<<ComboboxSelected>>", self._callback)
        self.monitorsCombo.current(0)
        self.prevCombo = self.monitorsCombo.current()
        self.hotkeyEntry = tk.Entry(self)
        self.hotkeyEntry.grid(row=0, column=1, padx=5, pady=5)
        self.hotkeyEntry.insert(0, '+'.join(str(i) for i in self.hotkeys[0]))
        self.saveButton = tk.Button(
            self, text='Save and quit', command=self.parent._save)
        self.saveButton.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    def _callback(self, arg):
        """
        The callback used to track the changes to the combobox.
        """

        self.hotkeys[self.prevCombo] = (self.hotkeyEntry.get().split('+'))
        self.hotkeyEntry.delete(0, tk.END)
        self.hotkeyEntry.insert(
            0, '+'.join(str(i) for i in self.hotkeys[self.monitorsCombo.current()]))
        self.prevCombo = self.monitorsCombo.current()
