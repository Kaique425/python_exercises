import os
import shutil

current_path = r"/home/kaique/Desktop/shutil_testes2"
new_path = r"/home/kaique/Desktop/shutil_testes"


for root, dirs, files in os.walk(current_path):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_path, file)
        shutil.move(old_file_path, new_file_path)
        print(f'O arquivo {file} foi movido')
