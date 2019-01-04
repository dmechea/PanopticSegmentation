#!/bin/bash

LIGHTCYAN='\033[1;36m'
NC='\033[0m'
DGREY='\033[1;30m'
WHITE='\033[1;37m'

echo -e "${WHITE}=========================================================${NC}"
echo -e "${LIGHTCYAN}Download results and perform local evaluation.. ${NC}"
echo -e "${WHITE}=========================================================${NC}"

sleep 3

if [ ! -d "PanopticResults" ]
then
  ./scripts/download_and_unpack_results.sh
else
  echo -e "${LIGHTCYAN}PanopticResults folder already exists, So skipping results download.... ${NC}"
  sleep 2
  echo -e "${LIGHTCYAN}If you need to redownload, delete the PanopticResults folder.... ${NC}"
fi

sleep 3

./scripts/eval_panoptic_results.sh
