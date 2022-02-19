import json

#creating json string
employee='{"firstname": "Tom","lastname": "Cruise","occupation": "Actor"}'

print("Before Parsing: ",employee)

#convert string to python dict
empjsondict=json.loads(employee)

print("After Parsing:")
print(empjsondict['lastname'])


