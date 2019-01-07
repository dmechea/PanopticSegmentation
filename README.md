# PanopticSegmentation
This Repository combines the MASK_RCNN algorithm for instance segmentation and DeepLabV2 Algorithm for semantic segmentation in order to produce predictions for the Panoptic Segmentation Challenge.

## In order to use, it's require to setup the repository first:

### Prerequisites
Make sure you have `Python 3.6` and `pip3 9.0.1` and `pipenv` (other pip versions may work, however they are untested)
**This also requires CUDA 9 and cuDNN to be installed on system.**

### Installation:
1. Clone repository

2. Enter Root directory:
```
cd PanopticSegmentation
```

3. Install dependencies:
```
pipenv install
```

## Usage

From inside the root directory:

1. Enter Virtual Env:

`pipenv shell`

2. Run the command:

`pipenv run start`

3. Follow the instructions in the menu to run either inference or evaluation of the dataset.
