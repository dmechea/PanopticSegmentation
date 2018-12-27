import os
import sys
import numpy as np
import json

# Root directory of the project
MASK_RCNN_ROOT_DIR = os.path.abspath("./dependencies/Mask_RCNN")
sys.path.append(MASK_RCNN_ROOT_DIR)
#

from dependencies.Mask_RCNN import mrcnn

from mrcnn import utils
import mrcnn.model as modellib
from mrcnn.model import log
import samples.coco.coco as coco

from pycocotools.coco import COCO

ROOT_DIR = os.path.abspath("./")
WEIGHTS_PATH = os.path.join(ROOT_DIR, 'weights')

MODEL_DIR = os.path.join(ROOT_DIR, "logs")

COCO_MODEL_PATH = os.path.join(WEIGHTS_PATH, "mask_rcnn_coco.h5")

# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

config = coco.CocoConfig()
# config.display()

COCO_DATA_DIR = os.path.abspath("./data/coco")
COCO_ANNOTATIONS_PATH = os.path.abspath("./data/coco/val2017/annotations/instances_val2017.json")

dataset = coco.CocoDataset()
dataset.load_coco(COCO_DATA_DIR, "val", "2017")
dataset.prepare()

model = modellib.MaskRCNN(mode="inference", config=config, model_dir=MODEL_DIR )
model.load_weights(COCO_MODEL_PATH, by_name=True)

# Need to pass in annotation file
valCocoLib = COCO(annotation_file=COCO_ANNOTATIONS_PATH)

cocoFormatResults = coco.evaluate_coco(model, dataset, valCocoLib, eval_type="segm", limit=10)

with open('data.json', 'w') as outfile:
    json.dump(cocoFormatResults, outfile)
