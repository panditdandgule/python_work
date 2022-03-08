import itertools
import operator
from itertools import accumulate

#help(itertools.accumulate)

x=[2,3,4,6]
g=itertools.accumulate([2,3,4,5],func=operator.add)


x=[i for i in g]

print(x)

g1=itertools.accumulate(x,func=operator.mul)
x=[i for i in g1]
print(x)

g2=itertools.accumulate(x,func=operator.truediv)
x=[i for i in g2]
print(x)
