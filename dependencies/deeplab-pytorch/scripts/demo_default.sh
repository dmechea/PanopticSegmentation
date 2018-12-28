#!/bin/bash

python demo.py --config config/cocostuff164k.yaml \
               --model-path ./data/models/deeplab_resnet101/cocostuff164k/cocostuff164k_iter100k.pth \
               --image-path 000000002685.jpg
