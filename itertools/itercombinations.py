import itertools
from itertools import combinations

help(itertools.combinations)

comb=itertools.combinations([9,10,2,1],2)

x=[i for i in comb]
print(x)