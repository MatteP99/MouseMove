import pyautogui as pag
import screeninfo, keyboard, csv, os, sys, apputils
from application import Application

#Restarts the script and decides whether to open the settings or not
def runCfg(val):
    apputils.writeConfigurationFile(val)
    #Restart script to run or not the configuration GUI
    os.execl(sys.executable, 'python', __file__, *sys.argv[1:])

hotkeys = []
#flag that determines the opening of the settings
cfgFlag = apputils.readConfigurationFile()
apputils.readHotkeys(hotkeys)
monitors = [(m.x, m.y, m.width, m.height) for m in screeninfo.get_monitors()]

if cfgFlag == "1":
    app = Application(monitors, hotkeys)
    app.master.title('MoveMouse')
    app.mainloop()
    runCfg("0")
else:
    for n, monitor in enumerate(monitors):
        hotkey = f'{hotkeys[n][0]}'
        x = monitor[2] / 2 + monitor[0]
        y = monitor[3] / 2 + monitor[1]
        keyboard.add_hotkey(hotkey, pag.moveTo, args=(x,y))

    keyboard.add_hotkey('alt+shift+s', runCfg, args=("1"))
    keyboard.wait('alt+shift+0')