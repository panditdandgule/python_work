from itertools import groupby

data = [("A",77),("V",66),("X",57),("A",27),("X",47),("V",67),("R",27),("A",47),("V",67)]
print(data)

data.sort(key=lambda x:x[0])
print(data)

iter=groupby(data,lambda x:x[0])

for key, lst in iter:
    print(key,list(lst))