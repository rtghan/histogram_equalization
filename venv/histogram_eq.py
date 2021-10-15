import cv2 as cv
import numpy as np
import os

source_dir = 'C:/Users/chane/OneDrive/Documents/school files/EE\proj/venv'
output_dir = 'C:/Users/chane/OneDrive/Documents/school files/EE\proj/venv'

for img in os.listdir(source_dir):

    image = cv.imread(f'{source_dir}/{img}', 0);
    equ = cv.equalizeHist(image)
    cv.imwrite(f'{output_dir}/{img}', equ)

