import os
import cv2
import pickle

def create_template_file(data_path, save_path, accepted_masks_names):
    templates = []

    # Проходим по каждой папке с классом символов
    for class_name in os.listdir(data_path):

        if class_name not in accepted_masks_names:
            continue

        class_path = os.path.join(data_path, class_name)

        # Проходим по каждому образцу символа в папке класса
        for symbol_file in os.listdir(class_path):
            symbol_path = os.path.join(class_path, symbol_file)

            # Загружаем изображение символа
            symbol_image = cv2.imread(symbol_path, cv2.IMREAD_GRAYSCALE)

            # Преобразуем изображение в графическую маску
            _, mask = cv2.threshold(symbol_image, 127, 255, cv2.THRESH_BINARY)

            # Добавляем графическую маску и имя класса в список templates
            templates.append({'mask': mask, 'class': class_name})

    # Сохраняем список templates в файл template.pkl
    with open(save_path, 'wb') as f:
        pickle.dump(templates, f)

# Путь к папке с данными
data_path = '/home/wantbeasleep/yirDetectKruk/masks/symbols'

# Путь для сохранения файла template.pkl
save_path = '/home/wantbeasleep/yirDetectKruk/masks/templates/shorttemplate.pkl'

# Разрешенные классы для масок
accepted_masks_names = {
    'E008': True,
    'E030': True,
    'E082': True,
    'E009': True,
    'E024': True,
    'E024': True,
    'E012': True,
    'E011': True,
    'E010': True,
    'E051': True,
    'E032': True,
    'E042': True,
    'E022': True,
    'E023': True,
    'E054': True,
    'E033': True,
    'E021': True,
}

# Создаем файл template.pkl
create_template_file(data_path, save_path, accepted_masks_names)