from itertools import accumulate
import operator

list1=[1,2,3,4,54,5]
result=accumulate(list1,operator.mul)

print(list(result))
