import cv2 as cv
import numpy as np
import requests
import json
import os

def format_response(json):
    response = json['result']['tags'][:5]

    format = []
    for item in response:
        keypair = {}
        keypair[item['tag']['en']] = item['confidence']
        format.append(keypair)
    return format

def tag(image_path, api_key, api_secret):
    response = requests.post(
        'https://api.imagga.com/v2/tags',
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')})
    return response.json()

def find_unmatched(labels):
    unmatched = []
    for key in labels:
        if len(labels[key]) == 0:
            unmatched.append(key)
    return unmatched

def fix_unmatched(src, api_key, api_secret, filepath):
    results = ''
    with open(filepath, 'r') as f:
        results = json.load(f)

    unmatched = find_unmatched(results)
    print(unmatched)

    while len(unmatched) != 0:
        for img in unmatched:
            try:
                fp = f'{src}/{img}.jpg'
                response = tag(fp, api_key, api_secret)
                print(img)
                results[img] = format_response(response)
                print(results[img])
            except:
                pass

        unmatched = find_unmatched(results)

    with open(f'{filepath}_fix.json', 'w') as f:
        f.write(json.dumps(results, indent=4))

# low contrast
src_lc = 'C:/Users/chane/Downloads/EE images/1000_0.2'
api_key_lc = 'acc_66f11f4492250e3'
api_secret_lc = '0a5ee31e0860fc345ffc7f89cfc0093a'
lc_results = 'low_contrast_results_reformat.json'

fix_unmatched(src_lc, api_key_lc, api_secret_lc, lc_results)

# histogram equalized
src_he = 'C:/Users/chane/Downloads/EE images/1000_he'
api_key_he = 'acc_9988fd927555e07'
api_secret_he = 'e1ffc4f522e8646c9831fae85b75ebc7'
he_results = 'he_results.json'

fix_unmatched(src_he, api_key_he, api_secret_he, he_results)

# grayscale
src_g = 'C:/Users/chane/Downloads/EE images/1000_g'
api_key_g = 'acc_4236451543209cd'
api_secret_g = '80ad18ed933d305b109e895d5770b1fd'
g_results = 'grayscale_results.json'

fix_unmatched(src_g, api_key_g, api_secret_g, g_results)
