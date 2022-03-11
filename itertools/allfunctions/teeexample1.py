from itertools import tee

x=[10,20,30,40]

result=list(tee(x,2))

for li in result:
    print(list(li))
