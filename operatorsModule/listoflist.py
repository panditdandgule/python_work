from functools import reduce
import operator

#using operator and reduce function
numbers=[[2,3],[4,5],[65,6],[98,34]]
print(reduce(operator.add,numbers))

#using itertools chain
from itertools import chain
print(list(chain(*numbers)))

print(reduce(operator.add,[1,2,3,4]))

#multipliction
print(reduce(operator.mul,[1,2,3]))

#division
print(reduce(operator.truediv,[2,3,4]))