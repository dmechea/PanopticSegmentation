#!/bin/bash

cd dependencies/deeplab-pytorch && ./scripts/setup_caffemodels.sh

cd dependencies/deeplab-pytorch &&
python convert.py --dataset coco_init
