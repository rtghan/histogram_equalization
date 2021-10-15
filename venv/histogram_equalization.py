import cv2 as cv
import numpy as np
import requests
import json

def histogram_eq(image_name):
    # read the image
    original_img = cv.imread(image_name);

    # convert to grayscale
    img = cv.cvtColor(original_img, cv.COLOR_BGR2GRAY)

    # calculate amount of pixels and channels
    channels = 256
    pixels = img.shape[0] * img.shape[1]

    # generate an array of size 256 to accomodate all 256 possible intensity values (8-bit)
    cumulative_intensity_hist = np.zeros(channels)

    for y in range(0, img.shape[0]): # this for loop runs for every row of pixels in the image
        for x in range(0, img.shape[1]): # this loop runs for every column of pixels in the image

            # image[y][x] returns the intensity value of the pixel at that column and row
            for intensity in range(img[y][x], channels):
                # to generate the cumulative intensity histogram, bins greater than and including the bin of the
                # pixel's intensity will be incremented by one
                cumulative_intensity_hist[intensity] += 1

    # generate an array of size 256 to accomodate all 256 possible intensity values (8-bit) for the lookup table
    lookup_table = np.zeros(channels)

    # calculate the lookup table with the cumulative intensity histogram
    for intensity in range(0, channels):

        # use the formula to calculate the adjusted value
        adjusted_val = (channels/pixels) * cumulative_intensity_hist[intensity] - 1

        # set the lookup table value to the adjusted value if it is over 0
        if adjusted_val >= 0:
            lookup_table[intensity] = round(adjusted_val)

        # it is 0 by default so no need to set the lookup table value to 0

    # adjust the intensities in the image
    for y in range(0, img.shape[0]): # this for loop runs for every row of pixels in the image
        for x in range(0, img.shape[1]): # this loop runs for every column of pixels in the image
            img.itemset((y, x), lookup_table[img[y][x]])

    cv.imwrite("he_image.jpg", img)

def tag(image_path):
    api_key = 'acc_66f11f4492250e3'
    api_secret = '0a5ee31e0860fc345ffc7f89cfc0093a'

    response = requests.post(
        'https://api.imagga.com/v2/tags',
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')})
    return response.json()

dir = 'C:/Users/chane/Downloads/EE images/grayscale_orig/'
# image = '2_d.jpg'
# img_eq = cv.equalizeHist(cv.imread(f'{dir}{image}', 0))
# cv.imwrite(f'{dir}test.png', img_eq)

# results = tag(f'C:/Users/chane/Downloads/EE images/1000/000026e7ee790996.jpg')['result']['tags'][:10]
results_eq = tag(f'{dir}test.png')
with open('jsonformat.json', 'w') as f:
    f.write(json.dumps(results_eq, indent=4))
# print(results)
print(results_eq)