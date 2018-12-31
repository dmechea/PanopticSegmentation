# stuffID => stuffName => PanopticName => PanopticID => PanopticIndex

import json
from utils import loadJson, loadStuffTextLabels

path_to_panoptic_classes = './dependencies/panopticapi/panoptic_coco_categories.json'
path_to_stuff_classes = './dependencies/deeplab-pytorch/data/datasets/cocostuff/labels_2.txt'


# In goes labels, out comes dictionary
def createStuffToPanopticClassDictionary(stuff_class_dict, panoptic_class_dict):
    print (stuff_class_dict)
    print (panoptic_class_dict)


# Panoptic categories is a list and I need to make a dictionary
# That ties the id to position in list
def panopticToIndexPosition(panoptic_category_json):
    resulting_dict = {}
    for index, classItem in enumerate(panoptic_category_json):
        id = classItem['id']
        resulting_dict[id] = index
    return resulting_dict


stuff_category_dict = loadStuffTextLabels(path_to_stuff_classes)
panoptic_category_dict = loadJson(path_to_panoptic_classes)

def convertStuffIDToPanopticIndex(id):
    strId = str(id) if not isinstance(id, str) else id
    stuff_id_name = stuff_category_dict[strId]
    print (stuff_id_name)

def stuffIdToPanopticIndex(stuff_id_dict, panoptic_index_dict):
    pass

convertStuffIDToPanopticIndex(97)

# panopticToIndexPosition(panoptic_category_json)
