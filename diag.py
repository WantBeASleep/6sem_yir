import pickle
import pprint

def a(path):
    with open(path, 'rb') as f:
        templates = pickle.load(f)
        classes = {}
        for temp in templates:
            name = temp['class']
            if name not in classes:
                classes[name] = 1
            else:
                classes[name] = classes[name] + 1

        pprint.pprint(classes)

a('/home/wantbeasleep/yirDetectKruk/masks/templates/template.pkl')
a('/home/wantbeasleep/yirDetectKruk/masks/templates/shorttemplate.pkl')