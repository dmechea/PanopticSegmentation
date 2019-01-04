#!/bin/bash

LIGHTCYAN='\033[1;36m'
NC='\033[0m'
DGREY='\033[1;30m'
WHITE='\033[1;37m'

echo -e "${LIGHTCYAN}Evaluating Results... ${NC}"

python dependencies/panopticapi/evaluation.py \
  --gt_json_file ./dataset/coco/val2017/annotations/panoptic_val2017.json \
  --pred_json_file ./PanopticResults/panoptic_val2017_MrcnnDeepLab2_results.json

echo -e "${LIGHTCYAN}----Done ${NC}"
