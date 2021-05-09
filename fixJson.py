import json,os
from glob import glob

PATH = 'data/'
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.json'))]

for x in result:
    print(x)
    with open(x,'r') as f:
        json_data = json.load(f)
        f.close()
    print(json_data)