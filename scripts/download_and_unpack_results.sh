#!/bin/bash

LIGHTCYAN='\033[1;36m'
NC='\033[0m'
DGREY='\033[1;30m'
WHITE='\033[1;37m'

echo -e "${LIGHTCYAN}Downloading val2017 Submission from dropbox host... ${NC}"

sleep 2

curl -L -o panoptic_val2017_MrcnnDeepLab2_results.zip "https://www.dropbox.com/s/s9uottyo7y3syhn/panoptic_val2017_MrcnnDeepLab2_results.zip?dl=0"

sleep 1

echo -e "${LIGHTCYAN}---Done ${NC}"

sleep 1

echo -e "${LIGHTCYAN}Extracting files... ${NC}"
mkdir PanopticResults

sleep 2

unzip panoptic_val2017_MrcnnDeepLab2_results.zip -d PanopticResults

echo -e "${LIGHTCYAN}---Done ${NC}"
