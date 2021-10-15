import cv2 as cv
import numpy as np
import os

source_dir = 'C:/Users/chane/Downloads/EE images/1000'
output_dir = 'C:/Users/chane/Downloads/EE images/1000_g'
for img in os.listdir(source_dir):
    img_orig = cv.imread(f'{source_dir}/{img}')
    # convert to grayscale
    grayscale = cv.cvtColor(img_orig, cv.COLOR_BGR2GRAY)
    cv.imwrite(f'{output_dir}/{img}', img_g)
