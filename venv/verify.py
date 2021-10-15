import json

def find_unmatched(labels):
    unmatched = []
    for key in labels:
        if len(labels[key]) == 0:
            unmatched.append(key)
    return unmatched

def verify(result):
    with open(result, 'r') as f:
        labels = json.load(f)
        print(str(result))
        print(find_unmatched(labels))

verify('lc_results_fix.json')
verify('he_results_fix.json')
verify('grayscale_results_fix.json')
# with open('lc_results_fix.json', 'r') as f:
#     lc = json.load(f)
#     print('lc')
#     print(find_unmatched(lc))
#
# with open('he_results_fix.json', 'r') as f:
#     he = json.load(f)
#     print('he')
#     print(find_unmatched(he))