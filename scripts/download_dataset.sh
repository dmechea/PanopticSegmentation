#!/bin/bash

LIGHTCYAN='\033[1;36m'
NC='\033[0m'

echo -e "${LIGHTCYAN}Downloading val2017 dataset from dropbox host... ${NC}"

sleep 1

echo -e "${LIGHTCYAN}Making dataset directory... ${NC}"
sleep 0.5
mkdir dataset
echo -e "${LIGHTCYAN}---Done ${NC}"
sleep 0.5

echo -e "${LIGHTCYAN}Downloading data... ${NC}"
sleep 0.5
cd dataset && curl -L -o coco.zip "https://www.dropbox.com/s/v2gl46mtp93ano9/coco.zip?dl=0" && cd ..
sleep 0.5

echo -e "${LIGHTCYAN}Extracting data... ${NC}"
unzip dataset/coco.zip -d dataset
