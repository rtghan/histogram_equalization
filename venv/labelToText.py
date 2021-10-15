import json

label_txt = {}
with open('labels.json', 'r') as f:
    labels = json.load(f)

    equivalents = {}

    with open('labelEquivalent.json', 'r') as l:
        equivalents = json.load(l)

    for key in labels:
        label_txt[key] = []
        print(f'{key}: {labels[key]}')
        for label in labels[key]:
            try:
                label_txt[key].append(equivalents[label])
            except:
                pass

with open('labels_txt.json', 'w') as f:
    f.write(json.dumps(label_txt, indent=4))
