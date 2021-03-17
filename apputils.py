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
        return [
            ('alt', 'shift', f'{n}')
            for n, _ in enumerate(screeninfo.get_monitors(), 1)
        ]


def read_settings_hotkeys():
    if os.path.exists(res_folder + 'settings_hotkeys.csv'):
        with open(res_folder + 'settings_hotkeys.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader]
    else:
        return [
            ('alt', 'shift', 's'),
            ('alt', 'shift', 'e')
        ]


def write_hotkeys(hotkeys, settings_hotkeys):
    """
    Write the hotkeys to the hotkeys.csv and settings_hotkeys.csv files.
    """
    with open(res_folder + 'hotkeys.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for n, _ in enumerate(hotkeys):
            writer.writerow(hotkeys[n])
    with open(res_folder + 'settings_hotkeys.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for n, _ in enumerate(settings_hotkeys):
            writer.writerow(settings_hotkeys[n])
