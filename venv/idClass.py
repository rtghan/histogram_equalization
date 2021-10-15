import json
import csv

path = 'C:/Users/chane/OneDrive/Documents/school files/EE/test-annotations-human-imagelabels.csv'

labels = {}

with open('C:/Users/chane/OneDrive/Documents/school files/EE/proj/venv/imageID_cleaned.txt', 'r') as f:
    for id in f:
        labels[str(id[:-1])] = []
try:
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if str(row[3]) == '1':
                labels[str(row[0])].append(str(row[2]))
except:
    pass

with open('labels.json', 'w') as j:
    j.write(json.dumps(labels, indent=4))

