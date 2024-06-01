import pprint
import pickle

with open('model.pickle', 'rb') as file:
    data = pickle.load(file)

# Красивый вывод содержимого файла
pprint.pprint(data)

