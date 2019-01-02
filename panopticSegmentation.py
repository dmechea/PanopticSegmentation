import os
import sys
import json
import yaml
from addict import Dict
from helpers import loadJson, makeResultsDirectory

mainConfig = Dict(yaml.load(open("./config.yaml")))

makeResultsDirectory(mainConfig.panoptic_results_folder)

# Root directory of the project
PANOPTIC_API = os.path.abspath(mainConfig.panopticapi_path)
sys.path.append(PANOPTIC_API)

from combine_semantic_and_instance_predictions import combine_predictions

instance_seg_path = './{}/{}.json'.format(mainConfig.results_folder, mainConfig.instance_result_json)
# instanceSegResults = loadJson(instance_seg_path)

semantic_seg_path = './{}/{}.json'.format(mainConfig.results_folder, mainConfig.semantic_result_json)
# semanticSegResults = loadJson(semantic_seg_path)

images_json_path = './{}/{}.json'.format(mainConfig.results_folder, mainConfig.panoptic_temp)
# images_json_file = loadJson(images_json_path)

panoptic_coco_categories = '{}/{}.json'.format(mainConfig.panopticapi_path, mainConfig.panoptic_cat_path)

# Out file
panoptic_segmentation_file = './{}/{}.json'.format(mainConfig.panoptic_results_folder, mainConfig.submission_name)


combine_predictions(
    semseg_json_file = semantic_seg_path,
    instseg_json_file = instance_seg_path,
    images_json_file = images_json_path,
    categories_json_file = panoptic_coco_categories,
    segmentations_folder = None,
    panoptic_json_file = panoptic_segmentation_file,
    confidence_thr = 0.5,
    overlap_thr = 0.5,
    stuff_area_limit = 0.5
)
