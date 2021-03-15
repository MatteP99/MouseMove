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

    def __init__(self, monitors, parent, master=None):
        super().__init__(master)
        self.monitors = monitors
        self.parent = parent
        self._createWidgets()

    def _createWidgets(self):
        """
        Creates the necessary widgets for the gui.
        """
   
        hotkeys = self.parent.get_hotkeys()
        vals = [f"Monitor {n}" for n, monitor in enumerate(self.monitors, 1)]
        self.monitorsCombo = tk.ttk.Combobox(
            self, values=vals, state="readonly")
        self.monitorsCombo.grid(row=0, column=0, padx=5, pady=5)
        self.monitorsCombo.bind("<<ComboboxSelected>>", self._callback)
        self.monitorsCombo.current(0)
        self.prevCombo = self.monitorsCombo.current()
        self.hotkeyEntry = tk.Entry(self)
        self.hotkeyEntry.grid(row=0, column=1, padx=5, pady=5)
        self.hotkeyEntry.insert(
            0, '+'.join(str(i) for i in hotkeys[0]))
        self.saveButton = tk.Button(
            self, text='Save and quit', command=self.parent.save)
        self.saveButton.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    def _callback(self, arg):
        """
        The callback used to track the changes to the combobox.
        """
        
        hotkeys = self.parent.get_hotkeys()
        hotkeys[self.prevCombo] = (self.hotkeyEntry.get().split('+'))
        self.parent.set_hotkeys(hotkeys)
        self.hotkeyEntry.delete(0, tk.END)
        self.hotkeyEntry.insert(
            0, '+'.join(str(i) 
            for i in hotkeys[self.monitorsCombo.current()]))
        self.prevCombo = self.monitorsCombo.current()
