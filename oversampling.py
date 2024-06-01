import os
from PIL import Image
import pprint
import random
import shutil

res = []

def process_images_in_folder(parent_folder):
    for root, _, files in os.walk(parent_folder):
        if os.path.basename(root) == "Symbols":
            continue
        res.append({
            "name": os.path.basename(root),
            "count": len(files),
        })

# Укажите путь к вашей основной папке, содержащей изображения
parent_folder = '/home/wantbeasleep/yirDetectKruk/Symbols'

# Обработка изображений в директории
process_images_in_folder(parent_folder)

res_sorted = sorted(res, key=lambda x: x['count'])

percentLen = int(0.9 * len(res_sorted))

percentElems = res_sorted[:percentLen]

avg = 0

for classed in percentElems:
    avg += classed['count']

avg = avg // percentLen

print(avg)

for root, _, files in os.walk(parent_folder):
    if os.path.basename(root) == "Symbols":
        continue
    diff = avg - len(files)
    while diff > 0:
        diff -= 1
        random_file = random.choice(files)
        file_name, file_extension = os.path.splitext(random_file)
        new_file_name = f"{file_name}_COPY{file_extension}"
        random_file_path = os.path.join(root, random_file)
        new_file_path = os.path.join(root, new_file_name)

        # Копирование случайного файла с новым именем
        shutil.copy(random_file_path, new_file_path)

        # Обновление списка файлов и уменьшение счетчика
        files.append(new_file_name)
