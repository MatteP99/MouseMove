import tkinter as tk
import csv, os

class Application(tk.Frame):
    def __init__(self, monitors, hotkeys, master=None):
        super().__init__(master)
        self.monitors = monitors
        self.hotkeys = hotkeys
        self.grid(padx=5, pady=5)
        self.createWidgets()

    def createWidgets(self):
        vals = [f"Monitor {n+1}" for n, monitor in enumerate(self.monitors)]
        self.monitorsCombo = tk.ttk.Combobox(self, values = vals, state="readonly")
        self.monitorsCombo.grid(row = 0, column = 0, padx=5, pady=5)        
        self.monitorsCombo.bind("<<ComboboxSelected>>", self.callback)
        self.monitorsCombo.current(0)
        self.prevCombo = self.monitorsCombo.current()
        self.hotkeyEntry = tk.Entry(self)
        self.hotkeyEntry.grid(row = 0, column = 1, padx=5, pady=5)
        self.hotkeyEntry.insert(0, f'{self.hotkeys[self.monitorsCombo.current()][0]}')
        self.saveButton = tk.Button(self, text='Save', command=self.save)
        self.saveButton.grid(row = 1, column = 1, padx=5, pady=5)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row = 1, column = 0, padx=5, pady=5)
    
    def callback(self, arg):
        self.hotkeys[self.prevCombo][0] = self.hotkeyEntry.get()
        self.hotkeyEntry.delete(0, tk.END)
        self.hotkeyEntry.insert(0, f'{self.hotkeys[self.monitorsCombo.current()][0]}')
        self.prevCombo = self.monitorsCombo.current()

    def save(self):
        self.hotkeys[self.prevCombo][0] = self.hotkeyEntry.get()
        with open('res' + os.path.sep + 'hotkeys.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for n, _ in enumerate(self.monitors):
                writer.writerow([f'{self.hotkeys[n][0]}'])
    