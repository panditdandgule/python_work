from functools import reduce

values=[1,2,3,4,5]

from functools import reduce
result = reduce(lambda item1,item2:item1+item2,values)
print(result)

