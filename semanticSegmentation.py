import sys
import os
import click
import cv2
import numpy as np

import torch
import torch.nn.functional as F

from addict import Dict
import yaml

from pycocotools import cocostuffhelper as cocostuff

from pycocotools.coco import COCO

DEEPLAB_ROOT_DIR = os.path.abspath("./dependencies/deeplab-pytorch")
sys.path.append(DEEPLAB_ROOT_DIR)

from libs.models import DeepLabV2_ResNet101_MSC
from libs.utils import dense_crf

# Related to visualization
def createLabels(configObj):
    LabelsPath = os.path.join(DEEPLAB_ROOT_DIR, configObj.LABELS)

    # Label list
    with open(LabelsPath) as f:
        classes = {}
        for label in f:
            label = label.rstrip().split("\t")
            classes[int(label[0])] = label[1].split(",")[0]

def loadUpModel(model_path, cuda=True):
    cuda = cuda and torch.cuda.is_available()
    device = torch.device("cuda" if cuda else "cpu")

    if cuda:
        current_device = torch.cuda.current_device()
        print("Running on", torch.cuda.get_device_name(current_device))
    else:
        print("Running on CPU")

    # Model
    model = DeepLabV2_ResNet101_MSC(n_classes=CONFIG.N_CLASSES)
    state_dict = torch.load(model_path, map_location=lambda storage, loc: storage)
    model.load_state_dict(state_dict)
    model.eval()
    model.to(device)
    return model

def preProcessImage(image):
    scale = CONFIG.IMAGE.SIZE.TEST / max(image.shape[:2])
    image = cv2.resize(image, dsize=None, fx=scale, fy=scale)
    image_original = image.astype(np.uint8)
    image -= np.array(
        [
            float(CONFIG.IMAGE.MEAN.B),
            float(CONFIG.IMAGE.MEAN.G),
            float(CONFIG.IMAGE.MEAN.R),
        ]
    )
    image = torch.from_numpy(image.transpose(2, 0, 1)).float().unsqueeze(0)
    image = image.to(device)


def makePrediction(config, image_path, model, crf=False):
    # Configuration
    CONFIG = Dict(yaml.load(open(config)))

    torch.set_grad_enabled(False)

    # Model
    model = DeepLabV2_ResNet101_MSC(n_classes=CONFIG.N_CLASSES)
    state_dict = torch.load(model_path, map_location=lambda storage, loc: storage)
    model.load_state_dict(state_dict)
    model.eval()
    model.to(device)

    # Image preprocessing
    image = cv2.imread(image_path, cv2.IMREAD_COLOR).astype(float)
    image = preProcessImage(image)

    # Inference
    output = model(image)
    output = F.interpolate(
        output, size=image.shape[2:], mode="bilinear", align_corners=True
    )
    output = F.softmax(output, dim=1)
    output = output.data.cpu().numpy()[0]

    if crf:
        output = dense_crf(image_original, output)
    labelmap = np.argmax(output, axis=0)

    cocoResFormat = cocostuff.segmentationToCocoResult(labelmap, '000000002685')

    return cocoResFormat

def predictAndCompileImages():
    pass


# thisDir = os.path.abspath('./')
#
# configPath = os.path.join(DEEPLAB_ROOT_DIR, 'config','cocostuff164k.yaml')
# imagePath = os.path.join(DEEPLAB_ROOT_DIR, '000000002685.jpg')
# modelPath = os.path.join(DEEPLAB_ROOT_DIR, 'data', 'models', 'deeplab_resnet101', 'cocostuff164k', 'cocostuff164k_iter100k.pth')
#
# x = makePrediction(configPath, imagePath, modelPath)
#
# print (x)

# if __name__ == "__main__":
#     main()
