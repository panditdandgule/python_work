import json

f=open('emp.json','r')
data=json.load(f)
for i in data:
    print(i)

f.close()

