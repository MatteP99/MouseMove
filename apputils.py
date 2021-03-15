import csv
import os
import screeninfo

folder = 'res' + os.path.sep


def readHotkeys():
    """
    Read the hotkeys from the hotkeys.csv file.
    If it does not exists, set standard hotkeys.
    """

    if os.path.exists(folder + 'hotkeys.csv'):
        with open(folder + 'hotkeys.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader]
    else:
        if not os.path.exists('res'):
            os.mkdir('res')
        return [
            ('alt', 'shift', f'{n}')
            for n, _ in enumerate(screeninfo.get_monitors(), 1)
        ]


def writeHotkeys(hotkeys):
    """
    Write the hotkeys from the hotkeys.csv file.
    """
    with open(folder + 'hotkeys.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for n, _ in enumerate(hotkeys):
            writer.writerow(hotkeys[n])

