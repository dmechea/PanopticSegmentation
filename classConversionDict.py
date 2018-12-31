# Needs to be done by hand

# conversionDictionary = {
#     '97': '188', # cabinet
# }

import json
from utils import loadJson

path_to_panoptic_classes = './dependencies/panopticapi/panoptic_coco_categories.json'

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

# panoptic_category_json = loadJson(path_to_panoptic_classes)

# panopticToIndexPosition(panoptic_category_json)
