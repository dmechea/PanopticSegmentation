import json

def loadJson(relative_file_location):
    with open(relative_file_location) as json_data:
        return json.load(json_data)
