import os
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

def makeResultsDirectory(dir_name):
    stringify_dir=str(dir_name)
    # Make Directory to story results if it doesnt exist
    if not os.path.exists(stringify_dir):
        print ("Folder doesn't exist, making now... : {}".format(stringify_dir))
        os.makedirs(stringify_dir)
