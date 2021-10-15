import csv
import json

path = 'C:/Users/chane/OneDrive/Documents/school files/EE/oidv6-class-descriptions.csv'

labelEquivalent = {}
with open(path, 'r', encoding='cp850') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        labelEquivalent[str(row[0])] = str(row[1])


with open('labelEquivalent.json', "w") as f:
    f.write(json.dumps(labelEquivalent, indent=4))
