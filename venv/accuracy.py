import json

lc_path = 'lc_results_fix.json'
he_path = 'he_results_fix.json'
g_path = 'grayscale_results_fix.json'
labels_path = 'labels_txt.json'

def load(path):
    with open(path, 'r') as f:
        return json.load(f)

lc = load(lc_path)
he = load(he_path)
g = load(g_path)
labels = load(labels_path)

results = {}

lc_labels = 0
he_labels = 0
g_labels = 0
num_labels = 0
lc_confidence = 0
he_confidence = 0
g_confidence = 0

for key in labels:
    for label in labels[key]:
        print(label)
        for prediction in lc[key]:
            print(prediction)
            for item in prediction:
                if item.lower() == label.lower():
                    lc_labels += 1
                    lc_confidence += prediction[item]
        for prediction in he[key]:
            print(prediction)
            for item in prediction:
                if item.lower() == label.lower():
                    he_labels += 1
                    he_confidence += prediction[item]
        for prediction in g[key]:
            print(prediction)
            for item in prediction:
                if item.lower() == label.lower():
                    g_labels += 1
                    g_confidence += prediction[item]
        num_labels += 1

results['lc'] = [lc_labels, lc_confidence/float(lc_labels)]
results['he'] = [he_labels, he_confidence/float(he_labels)]
results['g'] = [g_labels, g_confidence/float(g_labels)]
results['num_labels'] = num_labels

with open('final_results.json', 'w') as f:
    f.write(json.dumps(results, indent=4))