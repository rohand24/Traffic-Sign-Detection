from __future__ import division


import numpy as np
import pickle
import re
import os
from PIL import Image
import pdb
import shutil
import glob2


# Script config
path_to_all_image_files = '/shared/kgcoe-research/mil/road_sign_dataset'

dst_dir = "/home/rnd7528/git/darkflow/lisa_data/"
i=0
image_files = glob2.glob(path_to_all_image_files+'/**/*.png')
for image in image_files:
    shutil.copy(image, dst_dir)
    if i%100 == 0:
		print('iteration = '+ str(i))
    i=i+1
