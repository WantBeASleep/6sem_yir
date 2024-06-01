import os
import random
from PIL import Image, ImageDraw

def add_noise_to_image(image_path, output_folder, base_name):
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)
        width, height = img.size
        noise_size = int(0.05 * height)  # Размер точки шума - 5% от высоты картинки
        number_of_noises = random.randint(1, 5)  # Случайное количество точек шума от 1 до 5

        for _ in range(number_of_noises):
            # Случайные координаты для центра точки шума
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            # Рисуем квадрат как точку шума
            draw.rectangle([x, y, x + noise_size, y + noise_size], fill=(0, 0, 0))

        file_name, file_extension = os.path.splitext(base_name)
        new_filename = f"{file_name}_DIRTY{file_extension}"
        img.save(os.path.join(output_folder, new_filename))

def process_images_in_folder(parent_folder):
    for root, _, files in os.walk(parent_folder):
        for file in files:
            if file.endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                image_path = os.path.join(root, file)
                base_name = file
                add_noise_to_image(image_path, root, base_name)

# Укажите путь к вашей основной папке, содержащей изображения
parent_folder = '/home/wantbeasleep/yirDetectKruk/Symbols'

# Обработка изображений в директории
process_images_in_folder(parent_folder)
