import json

with open('jsonformat.json', 'r') as f:
    test = json.load(f)

    test2 = test['result']['tags'][:5]

    new = []
    for item in test2:
        keypair = {}
        keypair[item['tag']['en']] = item['confidence']
        new.append(keypair)
    print(new)
