import cv2
import numpy as np
import pickle
from PIL import Image as pim
from glob import glob
import os
import json

# Загрузка файла template.pkl
def load_templates(template_file_path):
    with open(template_file_path, 'rb') as f:
        templates = pickle.load(f)
    return templates

# Загрузка изображения рукописи и перевод в оттенки серого
def load_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return image
   

def get_detected_hooks_on_image(image, masks, mask_threshold: float = 0.65, per_class_limit: int = 3, delta_x: int = 10, delta_y: int = 10):
    """
        per_class_limit: ограничение по кол-ву детекту для класса сивмволов
        delta_x: минимальное расстояние для детекта символов по оси x
        delta_y: минимальное расстояние для детекта символов по оси y
    """

    # мапа [class] -> кол-во детект символов
    class_found = {}
    # найденные символы
    symbols_found = {}

    # Проходим по всем шаблонам
    for template in masks:
        mask = template['mask']
        class_name = template['class']

        if class_name not in class_found:
            class_found[class_name] = 0

        # скипаем если больше 3 изображений 1-го класса
        if class_found[class_name] > 3:
            continue

        template_height, template_width = mask.shape

        # Применяем метод шаблонного сопоставления
        res = cv2.matchTemplate(image, mask, cv2.TM_CCOEFF_NORMED)

        # Находим места, где корреляция выше порога
        loc = np.where(res >= mask_threshold)

        # Для каждого места, где корреляция выше порога, добавляем символ в список symbols_found
        for pt in zip(*loc[::-1]):
            class_found[class_name] += 1

            if class_name not in symbols_found:
                symbols_found[class_name] = []

            if len(symbols_found[class_name]) != 0 and abs(pt[0] - symbols_found[class_name][-1]['x']) < delta_x and abs(pt[1] - symbols_found[class_name][-1]['y']) < delta_y:
                continue

            """
                symbols_found - {}, key := className, val := массив из структуры 74-79 строчка
                надо в бд плюнуть в новую колонку для каждой страницы кол-во всех найденых крюков
                total := 0
                for _, k := range name {
                    total += len(k)
                }


                в фунцию get_detected_hooks_on_image прилетает еще masks - это template массив из 
                масок + имя класса
            """
            # symbols_found 
            # total := 0
            # for _, k := range name {
            #   total += len(k)
            # }
            # DB <--- total
 
            symbols_found[class_name].append({
                'x': int(pt[0]),
                'y': int(pt[1]),
                'width': int(template_width),
                'height': int(template_height)
            })

            # Обновляем изображение, закрашивая область символа белым и сдвигая текущую координату
            cv2.rectangle(image, (pt[0], pt[1]), (pt[0] + template_width, pt[1] + template_height), (255, 255, 255), -1)

    return symbols_found

# Пути к файлам и изображению
template_file_path = '/home/wantbeasleep/yirDetectKruk/masks/templates/shorttemplate.pkl'
 
def main():
    templates = load_templates(template_file_path)
    imagedir = os.path.join(os.path.dirname(__file__), 'wimages/*')
    
    pages = []

    for input_image in glob(imagedir):
        name = os.path.splitext(os.path.basename(input_image))[0]
        numpy_image = load_image(input_image)
        
        symbols_found = get_detected_hooks_on_image(numpy_image, templates, mask_threshold=0.8, per_class_limit=10)
        pages.append({
            'name': name,
            'found_symbols': symbols_found,
        })

        pim.fromarray(numpy_image).save('output/' + name + '.jpg')

    with open('output/res.json', 'w+') as json_file:
        json.dump(pages, json_file, indent=4)


if __name__ == "__main__":
    main()