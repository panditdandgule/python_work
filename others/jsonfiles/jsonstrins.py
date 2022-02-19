
#creating string
import json

employee='{"name":"pandit","age":32,"adr":"Pune"}'

employee_dict=json.loads(employee)

print(employee_dict)