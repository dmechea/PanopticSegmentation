#!/bin/bash

LIGHTCYAN='\033[1;36m'
NC='\033[0m'
WHITE='\033[1;37m'
LRED='\033[1;31m'

PS3='Please enter your choice: '
options=("Full installation and predict on dataset" "Install Dataset and models only" "Run Predictions only" "Download pre-made predictions and local evaluation (quickest)" "Quit")


echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo -e "${LIGHTCYAN}Hello!${NC}"
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""

sleep 2

echo -e "Welcome to my Panoptic Segmentation Challenge Repository."
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 3
echo -e "Before continuing, please ensure you have ${LRED}python 3.6${NC}....."
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 3
echo -e "..... and have run ${LRED}pipenv install${NC} to install all dependencies."
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 3
echo -e "And dont forget to run ${LRED}pipenv shell${NC} to run this program from a virtual env"
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 3
echo -e "If you have done that, then please select from the following options:"
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
echo -e "${WHITE}=========================================================${NC}"


select opt in "${options[@]}"
do
    case $opt in
        "Full installation and predict on dataset")
            echo -e "You Selected ${LIGHTCYAN}Full installation and predict on dataset${NC}"
            sleep 2
            echo ""
            echo ""
            echo -e "${WHITE}Working.....${NC}"
            echo -e ""
            echo -e ""
            sleep 1
            ./scripts/clone_to_zip.sh
            break
            ;;
        "Install Dataset and models only")
            echo -e "You Selected ${LIGHTCYAN}Install Dataset and models only${NC}"
            sleep 2
            echo ""
            echo ""
            echo -e "${WHITE}Working.....${NC}"
            echo -e ""
            echo -e ""
            sleep 1
            ./scripts/raw_repo_setup.sh
            break
            ;;
        "Run Predictions only")
            echo -e "You Selected ${LIGHTCYAN}Install Dataset and models only${NC}"
            sleep 2
            echo ""
            echo ""
            echo -e "${WHITE}Working.....${NC}"
            echo ""
            echo ""
            sleep 1
            ./scripts/run_inference_and_zip.sh
            break
            ;;
        "Download pre-made predictions and local evaluation (quickest)")
            echo -e "You Selected ${LIGHTCYAN}Download pre-made predictions and local evaluation${NC}"
            sleep 2
            echo ""
            echo ""
            echo -e "${WHITE}Working.....${NC}"
            echo ""
            echo ""
            sleep 1
            ./scripts/download_and_eval_results.sh
            break
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
