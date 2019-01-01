import os
import sys
import numpy as np
import json
import yaml
from addict import Dict

mainConfig = Dict(yaml.load(open("./config.yaml")))

# Root directory of the project
MASK_RCNN_ROOT_DIR = os.path.abspath(mainConfig.mrcnn_path)
sys.path.append(MASK_RCNN_ROOT_DIR)

# from dependencies.Mask_RCNN import mrcnn
from operator import itemgetter

from mrcnn import utils
import mrcnn.model as modellib
from mrcnn.model import log
import samples.coco.coco as coco
from pycocotools.coco import COCO

ROOT_DIR = os.path.abspath("./")
WEIGHTS_PATH = os.path.join(ROOT_DIR, 'weights')

MODEL_DIR = os.path.join(ROOT_DIR, "logs")

COCO_MODEL_PATH = os.path.join(ROOT_DIR, mainConfig.mrcnn_weights)

# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

config = coco.CocoConfig()
# config.display()

COCO_DATA_DIR = os.path.abspath(mainConfig.coco_dir)
COCO_ANNOTATIONS_PATH = os.path.abspath(mainConfig.coco_ann_path)

dataset = coco.CocoDataset()

if mainConfig.data_set == "val2017":
    dataset.load_coco(COCO_DATA_DIR, "val", "2017")
    dataset.prepare()
else:
    raise Exception('No other datasets can be used for now. Please use val2017')

model = modellib.MaskRCNN(mode="inference", config=config, model_dir=MODEL_DIR )
model.load_weights(COCO_MODEL_PATH, by_name=True)

# Need to pass in annotation file
valCocoLib = COCO(annotation_file=COCO_ANNOTATIONS_PATH)

lim = int(mainConfig.image_limit) if mainConfig.image_limit != 'None' else None

# Honestly this isn't needed but its pre-existing function which does the job i need it to
cocoFormatResults = coco.evaluate_coco(model, dataset, valCocoLib, eval_type="segm", limit=lim)

with open('Results/instanceSegmentationResults.json', 'w') as outfile:
    json.dump(cocoFormatResults, outfile)
