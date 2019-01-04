#!/bin/bash

LIGHTCYAN='\033[1;36m'
NC='\033[0m'

ZIP_NAME='panoptic_val2017_MrcnnDeepLab2_results'

echo -e "${LIGHTCYAN}Creating zip file for competition submission.... ${NC}"
sleep 0.5
echo -e "${LIGHTCYAN}Zipfile Name = ${ZIP_NAME}${NC}"
sleep 0.5
cd PanopticResults && zip -r "../${ZIP_NAME}.zip" *
echo -e "${LIGHTCYAN}----Done ${NC}"
