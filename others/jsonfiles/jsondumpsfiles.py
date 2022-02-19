import json

employee={'name':'pandit','age':32,'adr':'pune'}

f=open('emp1.json','w')

employee_json=json.dump(employee,f)

f.close()
