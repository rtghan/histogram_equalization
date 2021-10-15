import os
import csv

path = 'C:/Users/chane/OneDrive/Documents/school files/EE/test-annotations-human-imagelabels.csv'

with open(path, newline='') as cf:
    reader = csv.reader(cf, delimiter=',')
    counter = 0
    ids = ['000026e7ee790996']
    for row in reader:
        if counter > 1000:
            break
        if ids[counter] != row[0]:
            ids.append(row[0])
            counter += 1

    with open('imageID_cleaned.txt', "w") as f:
        for id in ids:
            f.write(f'{id}\n')



