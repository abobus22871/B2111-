import os
path_win = os.path.normpath("C:\Windows\Web")


for path, dirnames, filenames in os.walk(path_win):
    print(f"Шляхи до файлів та директорій - {path}")
    print(f"Папки - {dirnames}")
    print(f"Файли - {filenames}")