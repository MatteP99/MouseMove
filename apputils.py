import csv
import os

folder = 'res' + os.path.sep


def readHotkeys(hotkeys):
    with open(folder + 'hotkeys.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            hotkeys.append(row)


def writeHotkeys(hotkeys, monitors):
    with open(folder + 'hotkeys.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for n, _ in enumerate(monitors):
            writer.writerow([f'{hotkeys[n][0]}'])
