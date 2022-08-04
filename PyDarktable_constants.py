# File to store constants for PyDarktable.py

IMAGE_ROOT_DIR = '.'
INPUT_DIR = 'input/'
STAGE_1_PATH = 'stage_1/'
STAGE_1_DNG_PATH = 'images/stage_1/'
STAGE_2_PATH = 'stage_2/'
STAGE_2_DNG_PATH = 'images/stage_2/'
OUTPUT_DIR = 'output/'
OUTPUT_PREDICTIONS_DIR = 'predictions/'
DARKTABLE_DIR = "C:/Program Files/darktable/bin/darktable-cli.exe"
#DARKTABLE_DIR = "/opt/darktable/bin/darktable-cli"

class POSSIBLE_VALUES:
    def __init__(self):
        self.contrast =  [(-0.9, 0.9)]
        self.sharpen = [(0.0, 10.0)]
        self.exposure = [(-2.0, 4.0)]
        self.highlights = [(0.05, 0.4)] # highlights clipping threshold
