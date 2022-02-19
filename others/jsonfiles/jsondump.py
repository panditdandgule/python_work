import json

employee={'name':'pandit','age':32,'adr':'pune'}

employee_dict=json.dumps(employee,indent=4,sort_keys=True)

print(employee_dict)

