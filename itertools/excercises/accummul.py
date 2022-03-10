from itertools import accumulate
import operator

nums=[10,20,30,40,50]

result=list(accumulate(nums,operator.mul))
print(result)