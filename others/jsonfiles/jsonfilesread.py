import json

with open('emp.json','r') as f:
    data=json.load(f)

    for x,y in data.items():
        print(x,y)