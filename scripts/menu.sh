#!/bin/bash

LIGHTCYAN='\033[1;36m'
NC='\033[0m'
WHITE='\033[1;37m'
LRED='\033[1;31m'

PS3='Please enter your choice: '
options=("Full installation and predict on dataset" "Install Dataset and models only" "Run Predictions only" "Download pre-made predictions and local evaluation (quickest)" "Quit")

echo -e "${WHITE}=========================================================${NC}"
echo -e "${LIGHTCYAN}Hello! I see you have cloned the panopticSegmentation repo. ${NC}"
echo -e "${WHITE}=========================================================${NC}"

sleep 2

echo -e "${LIGHTCYAN}Before continuing, please ensure you have ${LRED}python 3.6${LIGHTCYAN}.....${NC}"
sleep 2
echo -e "${LIGHTCYAN}..... and have run ${LRED}pipenv install${LIGHTCYAN} to install all dependencies.${NC}"
sleep 2
echo -e "${LIGHTCYAN}.....${NC}"
sleep 0.2
echo -e "${LIGHTCYAN}.....${NC}"
sleep 0.2
echo -e "${LIGHTCYAN}..... oh! And dont forget to run ${LRED}pipenv shell${LIGHTCYAN} to run this program from a virtual env${NC}"
sleep 2
echo -e "${LIGHTCYAN}If you have done that, then please select from the following options: ${NC}"
echo -e "${WHITE}=========================================================${NC}"

sleep 1

select opt in "${options[@]}"
do
    case $opt in
        "Full installation and predict on dataset")
            echo "you chose choice 1"
            break
            ;;
        "Install Dataset and models only")
            echo "you chose choice 2"
            ;;
        "Run Predictions only")
            echo "you chose choice $REPLY which is $opt"
            ;;
        "Download pre-made predictions and local evaluation (quickest)")
            echo "Well done"
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
