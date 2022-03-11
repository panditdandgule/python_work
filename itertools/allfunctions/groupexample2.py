from itertools import groupby

items=[('A',27),('C',44),('D',33),('B',33),('C',54),('A',22),('E',23)]

items.sort(key=lambda x:x[0])
iter=groupby(items,lambda x:x[0])

for key,grp in iter:
    print(key,list(grp))