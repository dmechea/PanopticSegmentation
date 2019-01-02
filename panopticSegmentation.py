# from dependencies.panopticapi.combine_semantic_and_instance_predictions import combine_predictions

import os
import sys
import json

from helpers import loadJson

# Root directory of the project
PANOPTIC_API = os.path.abspath("./dependencies/panopticapi")
sys.path.append(PANOPTIC_API)

from combine_semantic_and_instance_predictions import combine_predictions

instance_seg_path = './Results/instanceSegmentationResults.json'
# instanceSegResults = loadJson(instance_seg_path)

semantic_seg_path = './Results/semanticSegmentationResults.json'
# semanticSegResults = loadJson(semantic_seg_path)

images_json_path = './Results/imagesJsonFile.json'
# images_json_file = loadJson(images_json_path)

panoptic_coco_categories = './dependencies/panopticapi/panoptic_coco_categories.json'

panoptic_segmentation_file = './Results/panopticSegmentationResults.json'


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
