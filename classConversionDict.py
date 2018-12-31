# Needs to be done by hand

# conversionDictionary = {
#     '97': '188', # cabinet
# }

import json

path_to_panoptic_classes = './dependencies/panopticapi/'



# In goes labels, out comes dictionary
def createStuffToPanopticClassDictionary(stuff_class_dict, panoptic_class_dict):
    print (stuff_class_dict)
    print (panoptic_class_dict)

# createStuffToPanopticClassDictionary('hi', 'bye')

# Panoptic categories is a list and I need to make a dictionary
# That ties the id to position in list
def panopticToIndexPosition(panoptic_category_json):
    resulting_dict = {}
    for index, classItem in enumerate(panoptic_category_json):
        id = classItem['id']
        resulting_dict[id] = index
    print (resulting_dict)
    return resulting_dict
