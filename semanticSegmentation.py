import sys
import os
import click
import cv2
import numpy as np
from glob import glob
from tqdm import tqdm
import json

from classConversionDict import convertStuffIdToPanopticId

import torch
import torch.nn.functional as F

from addict import Dict
import yaml

from pycocotools import cocostuffhelper as cocostuff

from pycocotools.coco import COCO

mainConfig = Dict(yaml.load(open("./config.yaml")))

DEEPLAB_ROOT_DIR = os.path.abspath(mainConfig.deeplab_path)

sys.path.append(DEEPLAB_ROOT_DIR)

from libs.models import DeepLabV2_ResNet101_MSC
from libs.utils import dense_crf

# Related to visualization
def createLabels(config_obj):
    LabelsPath = os.path.join(DEEPLAB_ROOT_DIR, config_obj.LABELS)

    # Label list
    with open(LabelsPath) as f:
        classes = {}
        for label in f:
            label = label.rstrip().split("\t")
            classes[int(label[0])] = label[1].split(",")[0]

def loadModel(model_path, config_obj, cuda=True):
    cuda = cuda and torch.cuda.is_available()
    device = torch.device("cuda" if cuda else "cpu")

    if cuda:
        current_device = torch.cuda.current_device()
        print("Running on", torch.cuda.get_device_name(current_device))
    else:
        print("Running on CPU")

    # Model
    model = DeepLabV2_ResNet101_MSC(n_classes=config_obj.N_CLASSES)
    state_dict = torch.load(model_path, map_location=lambda storage, loc: storage)
    model.load_state_dict(state_dict)
    model.eval()
    model.to(device)
    return model

def preProcessImage(image, config_obj, cuda=True):
    cuda = cuda and torch.cuda.is_available()
    device = torch.device("cuda" if cuda else "cpu")

    # This is causing issues as it is not same shape as inst segm.

    # scale = config_obj.IMAGE.SIZE.TEST / max(image.shape[:2])
    # image = cv2.resize(image, dsize=None, fx=scale, fy=scale)
    # image_original = image.astype(np.uint8)
    # image -= np.array(
    #     [
    #         float(config_obj.IMAGE.MEAN.B),
    #         float(config_obj.IMAGE.MEAN.G),
    #         float(config_obj.IMAGE.MEAN.R),
    #     ]
    # )
    image = torch.from_numpy(image.transpose(2, 0, 1)).float().unsqueeze(0)
    image = image.to(device)
    return image

def extractConfig(config_path):
    return Dict(yaml.load(open(config_path)))

def extractJpgImagePaths(image_folder):
    return glob(os.path.join(image_folder, '*.jpg'))

def extractIdFromPath(image_path):
    image_file = image_path.split('/')[-1]
    return image_file.split('.')[0]

def makePrediction(config_obj, image_path, model, cuda=True, crf=False):
    torch.set_grad_enabled(False)

    image_id = extractIdFromPath(image_path)

    # Image preprocessing
    image = cv2.imread(image_path, cv2.IMREAD_COLOR).astype(float)
    image = preProcessImage(image, config_obj, cuda)

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

    cocoResFormat = cocostuff.segmentationToCocoResult(labelmap, image_id)

    return cocoResFormat

# I cant create a JSON file as the segmentation is stores as bytes, need to decode
def decodeSegmentationResults(result_list):
    decoded_results = []
    for result in result_list:
        result_copy = Dict(result)
        encodedCounts = result_copy.segmentation.counts
        result_copy.segmentation.counts = encodedCounts.decode('utf8')

        decoded_results.append(result_copy)

    return decoded_results

def convertClassesForPanoptic(result_list):
    converted_results = []
    for result in result_list:
        result_copy = Dict(result)
        categoryClass = result_copy.category_id
        panopticIndex = convertStuffIdToPanopticId(categoryClass)
        if panopticIndex is not None:
            result_copy.category_id = panopticIndex
            converted_results.append(result_copy)
        else:
            print ('UH OH THERE IS NO PANOPTIC INDEX, Filtering for now')

    return converted_results

def runPredictions(model_path, config_path, image_folder, cuda=True, limit=None):
    config_obj = extractConfig(config_path)
    model = loadModel(model_path, config_obj, cuda)

    image_path_list = sorted(extractJpgImagePaths(imageFolder))

    image_range = limit if limit is not None else len(image_path_list)

    total_results = []

    for index in tqdm(range(image_range)):
        image_path = image_path_list[index]
        image_results = makePrediction(config_obj, image_path, model)
        total_results.extend(image_results)

    decoded_results = decodeSegmentationResults(total_results)
    class_conversion = convertClassesForPanoptic(decoded_results)

    print (len(class_conversion))

    with open('Results/semanticSegmentationResults.json', 'w') as outfile:
        json.dump(class_conversion, outfile)
        print ('JSON file created in Results folder')


thisDir = os.path.abspath('./')

modelPath = os.path.join(DEEPLAB_ROOT_DIR, 'data', 'models', 'deeplab_resnet101', 'cocostuff164k', 'cocostuff164k_iter100k.pth')
configPath = os.path.join(DEEPLAB_ROOT_DIR, 'config','cocostuff164k.yaml')
imageFolder = os.path.join(thisDir, 'dataset', 'coco', 'val2017')

lim = int(mainConfig.image_limit) if mainConfig.image_limit != 'None' else None

runPredictions(modelPath, configPath, imageFolder, limit=lim)

# if __name__ == "__main__":
#     main()
