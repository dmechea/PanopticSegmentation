import json
import yaml
from addict import Dict
from helpers import loadJson

mainConfig = Dict(yaml.load(open("./config.yaml")))

panoptic_gt_dict = loadJson(mainConfig.panoptic_gt_json_path)

panoptic_gt_dict.pop('annotations')
panoptic_gt_dict.pop('categories')

with open('{}/{}.json'.format(mainConfig.results_folder, mainConfig.panoptic_temp), 'w') as outfile:
    json.dump(panoptic_gt_dict, outfile)

print ('Successfully created baseline json file for panoptic results')
print ('File: {}/{}.json'.format(mainConfig.results_folder, mainConfig.panoptic_temp))
