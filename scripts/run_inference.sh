#!/bin/bash

LIGHTCYAN='\033[1;36m'
NC='\033[0m'

echo -e "${LIGHTCYAN}Running Inference For Panoptic Analysis ${NC}"

# echo "Checking that validation data is ready and set up......"
#
# echo "NEED DATA BEFORE ANYTHING"
#
# echo "Running instance segmentation on data set"

sleep 0.5

echo -e "${LIGHTCYAN}Running instance segmentation, using MASK_RCNN ${NC}"

python instanceSegmentation.py

echo -e "${LIGHTCYAN}---Done ${NC}"

sleep 0.5

echo -e "${LIGHTCYAN}Running semantic segmentation, using deeplab-V2 ${NC}"

python semanticSegmentation.py

echo -e "${LIGHTCYAN}----Done ${NC}"

sleep 0.5

echo -e "${LIGHTCYAN}Creating images json to store panoptic results... ${NC}"

python createPanopticResultsImageFile.py

echo -e "${LIGHTCYAN}----Done ${NC}"


echo -e "${LIGHTCYAN}Combining Segmentations to produce panoptic results ${NC}"
