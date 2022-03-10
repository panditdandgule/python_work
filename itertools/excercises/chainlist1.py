from itertools import chain

result=[[1,2,3,4],['a','b','c','d'],[10,20,30,40]]

newlist=chain(*result)

print(list(newlist))