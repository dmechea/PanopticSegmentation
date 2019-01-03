import os
import sys
from addict import Dict
import yaml

mainConfig = Dict(yaml.load(open("./config.yaml")))

# Root directory of the project
MASK_RCNN_ROOT_DIR = os.path.abspath(mainConfig.mrcnn_path)
sys.path.append(MASK_RCNN_ROOT_DIR)

from mrcnn import utils

ROOT_DIR = os.path.abspath("./")
COCO_MODEL_PATH = os.path.join(ROOT_DIR, mainConfig.mrcnn_weights)

# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)
