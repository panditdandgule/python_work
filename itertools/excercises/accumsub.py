from itertools import accumulate
import operator

nums=(10,20,30,40)

result=list(accumulate(nums,operator.sub))

print(result)
