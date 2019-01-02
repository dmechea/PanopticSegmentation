#!/bin/bash

python dependencies/panopticapi/evaluation.py \
  --gt_json_file ./dataset/coco/val2017/annotations/panoptic_val2017.json \
  --pred_json_file ./Results/panopticSegmentationResults.json
