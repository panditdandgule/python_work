from collections import OrderedDict

stud=OrderedDict()

n=int(input("Enter Number of subjects: "))

new_list=[]
for i in range(n):
    subject=input("Input Subject name and marks").split(' ')
    new_list.append(subject)

for item in new_list:
    print(item)

