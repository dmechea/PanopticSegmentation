#!/bin/bash

cd dependencies/deeplab-pytorch && ./scripts/setup_caffemodels.sh

python convert.py --dataset coco_init
