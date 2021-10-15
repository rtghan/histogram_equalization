import cv2 as cv
import numpy as np
import requests
import json
import os

def tag(image_path):
    api_key = 'acc_66f11f4492250e3'
    api_secret = '0a5ee31e0860fc345ffc7f89cfc0093a'

    response = requests.post(
        'https://api.imagga.com/v2/tags',
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')})
    return response.json()

def setup_json():
    responses = {}
    with open('labels_txt.json') as f:
        labels = json.load(f)
        for key in labels:
            responses[key] = []
    return responses

def format_response(json):
    response = json['result']['tags'][:5]

    format = []
    for item in response:
        keypair = {}
        keypair[item['tag']['en']] = item['confidence']
        format.append(keypair)
    return format

# low contrast dir
src = 'C:/Users/chane/Downloads/EE images/1000_0.2'

# histogram equalized dir
# src = 'C:/Users/chane/Downloads/EE images/1000_he'

# grayscale dir
# src = 'C:/Users/chane/Downloads/EE images/1000_g'

responses = setup_json()

for img in os.listdir(src):
    try:
        result = tag(f'{src}/{img}')
        print(img[:-4])
        responses[img[:-4]] = format_response(result)
        print(responses[img[:-4]])
    except:
        pass

with open('low_contrast.json', 'w') as f:
    f.write(json.dumps(responses, indent=4))


