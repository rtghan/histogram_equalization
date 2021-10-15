import json

with open('low_contrast_results.json', 'r') as f:
    reformat = json.load(f)
    with open('low_contrast_results_reformat.json', 'w') as w:
        w.write(json.dumps(reformat, indent=4))