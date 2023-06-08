import os

HOME = os.environ['HOME']
DOWN = f'{HOME}/Downloads'

def humanize(val, iB=True):
    value = val
    if iB:
        units = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']
        base = 1024
    else:
        units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        base = 1000

    iu = 0  # Índice de unidades
    iu_max = len(units) - 1

    while (value / base) >= 1:
        if iu >= iu_max:
            break
        else:
            iu += 1

        value = value / base

    return f'{round(value, 2)} {units[iu]}'


def show_files(directory):
    print(f'{directory}:')

    for root, dirs, files in os.walk(directory):
        for file in files:
            path_file = os.path.join(root, file)
            if os.path.isfile(path_file) and not os.path.islink(path_file):
                size = os.path.getsize(path_file)
                print(f'  {file} -> {humanize(size)}')


def main():
    show_files(DOWN)


if __name__ == '__main__':
    main()
