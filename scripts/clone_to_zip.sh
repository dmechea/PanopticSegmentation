#!/bin/bash

LIGHTCYAN='\033[1;36m'
NC='\033[0m'
DGREY='\033[1;30m'
WHITE='\033[1;37m'

echo -e ""
echo -e ""
echo -e ""
echo -e ""
echo -e ""
echo -e ""
echo -e ""
echo -e ""
echo -e "${LIGHTCYAN}Full installation and predict on dataset${NC}"
echo -e ""
echo -e ""
echo -e ""
echo -e ""
echo -e ""
echo -e ""
echo -e ""
echo -e ""
echo -e ""
echo -e "Heres the contents:"
echo -e " "
echo -e "${WHITE}- Download coco val2017 with annotations.${NC}"
echo -e " "
echo -e "${WHITE}- Setup MASK_RCNN${NC}"
echo -e " "
echo -e "${WHITE}- Setup DeepLabV2${NC}"
echo -e " "

sleep 5

echo -e "${LIGHTCYAN}Ok! Let's begin. ${NC}"

sleep 2

./scripts/raw_repo_setup.sh
./scripts/run_inference_and_zip.sh
