import os
import sys
import numpy as np
import json

# Root directory of the project
MASK_RCNN_ROOT_DIR = os.path.abspath("./dependencies/Mask_RCNN")
sys.path.append(MASK_RCNN_ROOT_DIR)

from mrcnn import utils
import mrcnn.model as modellib
from mrcnn.model import log
import samples.coco.coco as coco
