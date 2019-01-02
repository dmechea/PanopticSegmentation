#!/bin/bash

cd dependencies/deeplab-pytorch && ./scripts/setup_caffemodels.sh

python convert.py --dataset coco_init

cd data/models/deeplab_resnet101/cocostuff164k && curl -L -o cocostuff164k_iter100k.pth "https://www.dropbox.com/s/vzs04q1wbohj8rd/cocostuff164k_iter100k.pth?dl=0"
