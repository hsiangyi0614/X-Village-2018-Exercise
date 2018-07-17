import json

with open('bbb.json') as f:
    bbb = json.load(f)
    print(bbb)
    print(json.dumps(bbb, indent=4))
