# stuffID => stuffName => PanopticName => PanopticID => PanopticIndex
# Do i need the panopticID? Maybe not

import json
from helpers import loadJson, loadStuffTextLabels

path_to_panoptic_classes = './dependencies/panopticapi/panoptic_coco_categories.json'
path_to_stuff_classes = './dependencies/deeplab-pytorch/data/datasets/cocostuff/labels_2.txt'

# Panoptic categories is a list and I need to make a dictionary
# That ties the id to position in list
def panopticToIndexPosition(panoptic_category_json):
    resulting_dict = {}
    for index, classItem in enumerate(panoptic_category_json):
        id = classItem['id']
        resulting_dict[str(id)] = index
    return resulting_dict

def makePanopticIdIndex(panoptic_category_list):
    panopticClassDict = {}
    for category in panoptic_category_list:
        name = category['name']
        id = category['id']
        panopticClassDict[str(id)] = name
    return panopticClassDict

def getAllMergedClasses(panoptic_category_dict):
    mergedClasses = {}
    for category in panoptic_category_dict:
        name = category['name']
        id = category['id']
        removedMergedName = name.split('-')[0]
        if 'merged' in name:
            mergedClasses[removedMergedName] = id
    return mergedClasses


stuff_category_dict = loadStuffTextLabels(path_to_stuff_classes)
panoptic_category_list = loadJson(path_to_panoptic_classes)

panopticClassIdDict = makePanopticIdIndex(panoptic_category_list)
panopticIdToIndexDict = panopticToIndexPosition(panoptic_category_list)
panopticMergedClassesDict = getAllMergedClasses(panoptic_category_list)

ids = list(panopticClassIdDict.keys())

def checkForMatch(stuffName):
    for id in ids:
        if stuffName in panopticClassIdDict[id]:
            print (id, panopticClassIdDict[id])

checkForMatch('blender')

# clothes, 105 is unnacounted for. What category can i slot it into? :/
manualDictConv = {
    94: 184, # Branch => tree-merged
    96: 197, # Building => building-other-merged
    97: 193, # Bush => grass merged (could go to tree-merged, tough call)
    98: 188, # cabinet => cabinet merged
    99: 185, # cage => fence merged
    101: 190, # carpet => floor-other-merged (could be 200?)
    102: 186, # ceiling-other to ceiling merged
    103: 186, # ceiling merged
    104: 189, # cloth => table-merged
    106: 187, # clouds => sky-merged
    110: 189, # desk-stuff => table-merged
    111: 194, # dirt => dirt-merged
    113: 185, # fence => fence-merged
    114: 190, # floor-marble => floor-other-merged
    115: 190, # floor-other => floor-other-merged
    116: 190, # floor-stone => floor-other-merged
    117: 190, # floor-tile => floor-other-merged
    120: 187, # fog => sky-other-merged (not really sky but where else? water merged?)
    121: 196, # food-other => food-other-merged
}

# I want this to return the correct class Number
def convertStuffIdToPanopticId(id):
    id = int(id) + 1
    strId = str(id) if not isinstance(id, str) else id
    stuff_id_name = stuff_category_dict.get(strId)
    panoptic_id_name = panopticClassIdDict.get(strId)
    #
    # print (strId, stuff_id_name)
    #
    if stuff_id_name == panoptic_id_name:
        return int(strId)
    else:
        mergedDictResult = panopticMergedClassesDict.get(stuff_id_name)
        if mergedDictResult is not None:
            return int(mergedDictResult)
        return mergedDictResult

# Stuff id will be 1 less than expected,
# then run above function and use pan dict to convert to idx
# maybe make it less functional to reduce imports as the paths will be hardcoded

# redundant
# def stuffIdToPanopticIndex(
#     id,
# ):
#     stuff_id_matched = int(id) + 1
#     pan_id = convertStuffIDToPanopticIndex(
#         stuff_id_matched,
#         panopticClassIdDict,
#         stuff_category_dict,
#         panopticMergedClassesDict
#     )
#
#     if pan_id is not None:
#         return panopticIdToIndexDict[pan_id]
#     else:
#         return None
