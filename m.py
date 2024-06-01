import os
import matplotlib.pyplot as plt

def count_images_in_folders(parent_folder):
    class_counts = {}

    # Проходимся по всем подпапкам в указанной папке
    for root, dirs, files in os.walk(parent_folder):
        for directory in dirs:
            class_folder = os.path.join(root, directory)
            # Подсчитываем количество файлов изображений в каждой папке-классе
            image_count = len([file for file in os.listdir(class_folder) if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))])
            class_counts[directory] = image_count

    return class_counts

def plot_class_distribution(class_counts, output_file):
    # Построение столбчатой диаграммы
    classes = list(class_counts.keys())
    counts = list(class_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(classes, counts, color='skyblue')
    
    plt.xlabel('Классы')
    plt.ylabel('Количество изображений')
    plt.title('Распределение количества изображений по классам')
    plt.xticks(rotation=90)
    
    plt.tight_layout()
    # Сохранение диаграммы в файл
    plt.savefig(output_file, format='png')
    plt.close()

# Укажите путь к вашей основной папке, содержащей подпапки с изображениями
parent_folder = '/home/wantbeasleep/yirDetectKruk/Symbols'
# Укажите путь и имя для сохранения изображения диаграммы
output_file = 'class_distribution.png'

# Получение количества изображений в каждой подпапке-классе
class_counts = count_images_in_folders(parent_folder)

# Построение и сохранение столбчатой диаграммы
plot_class_distribution(class_counts, output_file)