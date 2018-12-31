import json

def loadJson(relative_file_location):
    with open(relative_file_location) as json_data:
        return json.load(json_data)

def addOneToString(stringInt):
    return str(int(stringInt) + 1)

def loadStuffTextLabels(relative_file_location):
    file = open(relative_file_location, 'r')
    stuffLabels = {}
    for line in file:
        id, name = line.strip().split('\t')
        stuffLabels[addOneToString(id)] = name
    return stuffLabels
