#!/bin/bash

python dependencies/panopticapi/evaluation.py \
  --gt_json_file ./dataset/coco/annotations/panoptic_val2017.json \
  --pred_json_file ./Results/panopticSegmentationResults.json
