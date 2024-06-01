import os
from PIL import Image

def resize_and_save_image(original_image_path, output_folder, base_name, sizes):
    with Image.open(original_image_path) as img:
        for size in sizes:
            resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
            file_name, file_extension = os.path.splitext(base_name)
            new_filename = f"{size}_{file_name}{file_extension}"
            resized_img.save(os.path.join(output_folder, new_filename))

def process_images_in_folder(parent_folder):
    sizes = [256, 128, 64]
    for root, _, files in os.walk(parent_folder):
        for file in files:
            if file.endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                original_image_path = os.path.join(root, file)
                base_name = file
                resize_and_save_image(original_image_path, root, base_name, sizes)

# Укажите путь к вашей основной папке, содержащей изображения
parent_folder = '/home/wantbeasleep/yirDetectKruk/Symbols'

# Обработка изображений в директории
process_images_in_folder(parent_folder)
