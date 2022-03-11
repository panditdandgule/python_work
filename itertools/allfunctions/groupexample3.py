from itertools import groupby
import random

#subjects = ["Phy","Chem","Math"]
#marks = [(subjects[random.randint(0,2)],random.randint(35,100)) for item in range(30)]
marks=[('Math', 96), ('Chem', 47), ('Phy', 79), ('Math', 39), ('Math', 43), ('Math', 86), ('Phy', 89), ('Phy', 92), ('Chem', 91), ('Math', 46), ('Math', 44), ('Math', 83), ('Phy', 80), ('Math', 38), ('Chem', 88), ('Phy', 46), ('Phy', 85), ('Math', 97), ('Chem', 50), ('Phy', 99), ('Math', 93), ('Chem', 50), ('Chem', 71), ('Phy', 83), ('Chem', 91), ('Chem', 98), ('Phy', 91), ('Chem', 81), ('Math', 49), ('Math', 76)]

print(marks)

marks.sort(key=lambda x:x[0])

iter=groupby(marks,lambda x:x[0])

for key,grp in iter:
    print(key,list(grp))
