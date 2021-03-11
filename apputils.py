import csv
import os

folder = 'res' + os.path.sep

def readConfigurationFile():
    with open(folder + 'runCfg.csv',  newline='') as cfgFile:
        reader = csv.reader(cfgFile)
        for row in reader:
            return row[0]

def writeConfigurationFile(val):
    with open(folder + 'runCfg.csv', 'w', newline='') as cfgaFile:
        writer = csv.writer(cfgaFile)
        writer.writerow([val])

def readHotkeys(hotkeys):
    with open(folder + 'hotkeys.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            hotkeys.append(row)
