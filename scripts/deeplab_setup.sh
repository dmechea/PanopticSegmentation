#!/bin/bash

LIGHTCYAN='\033[1;36m'
NC='\033[0m'
DGREY='\033[1;30m'
WHITE='\033[1;37m'

echo -e "${WHITE}=========================================================${NC}"
echo -e "${LIGHTCYAN}Setting up deeplab model... ${NC}"
echo -e "${WHITE}=========================================================${NC}"

sleep 1

echo -e "${LIGHTCYAN}Downloading caffemodel, this may take some time, please go grab a coffee and relax... ${NC}"
echo -e "${WHITE}=========================================================${NC}"

sleep 5

cd dependencies/deeplab-pytorch && ./scripts/setup_caffemodels.sh

sleep 1

echo -e "${LIGHTCYAN}Caffe Model Installed! Now, Converting to Pytorch..... ${NC}"
echo -e "${WHITE}=========================================================${NC}"

sleep 3

python convert.py --dataset coco_init

sleep 1

echo -e "${LIGHTCYAN}---Done! ${NC}"
echo -e "${WHITE}=========================================================${NC}"

sleep 1

echo -e "${LIGHTCYAN}Downloading COCO Weights....... ${NC}"
echo -e "${WHITE}=========================================================${NC}"

cd data/models/deeplab_resnet101/cocostuff164k && curl -L -o cocostuff164k_iter100k.pth "https://www.dropbox.com/s/vzs04q1wbohj8rd/cocostuff164k_iter100k.pth?dl=0"

echo -e "${LIGHTCYAN}All Done! Deeplab Model is ready to run ${NC}"
echo -e "${WHITE}=========================================================${NC}"
