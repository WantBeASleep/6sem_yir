import os

def delete_files_with_underscores(parent_folder):
    for root, _, files in os.walk(parent_folder):
        for file in files:
            if file.count('_') >= 2:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

# Укажите путь к вашей основной папке
parent_folder = '/home/wantbeasleep/yirDetectKruk/Symbols'

# Удаление файлов
delete_files_with_underscores(parent_folder)
