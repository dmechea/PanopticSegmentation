import os
import sys
import numpy as np
import json

# Root directory of the project
# MASK_RCNN_ROOT_DIR = os.path.abspath("./dependencies/Mask_RCNN")
# sys.path.append(MASK_RCNN_ROOT_DIR)
#
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
