import csv
import os
import screeninfo

res_folder = 'res' + os.path.sep
monitors = [(m.x, m.y, m.width, m.height) for m in screeninfo.get_monitors()]


def read_hotkeys():
    """
    Read the hotkeys from the hotkeys.csv file.
    If it does not exists, set standard hotkeys.
    """

    if os.path.exists(res_folder + 'hotkeys.csv'):
        with open(res_folder + 'hotkeys.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader]
    else:
        if not os.path.exists('res'):
            os.mkdir('res')
        hotkeys = [
            ['alt', 'shift', f'{n}']
            for n, _ in enumerate(screeninfo.get_monitors(), 1)
        ]
        hotkeys.append(['alt', 'shift', 's'])
        hotkeys.append(['alt', 'shift', 'e'])
        return hotkeys


def write_hotkeys(hotkeys):
    """
    Write the hotkeys to the hotkeys.csv file.
    """
    with open(res_folder + 'hotkeys.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for n, _ in enumerate(hotkeys):
            writer.writerow(hotkeys[n])
