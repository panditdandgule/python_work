from itertools import accumulate
import operator

def find_maxmimum(nums):
    return accumulate(nums,max)

#list
result=find_maxmimum([1,3,2,7,9,8,10,11,12,14,11,12,7])
print(list(result))

#Tuple
result=find_maxmimum((1,7,7,6,5,4,3,2,8,1,2,3,10))
print("Returning Maximum values",list(result))


def find_minimum(nums):
    return accumulate(nums,min)

minresult=find_minimum((7,7,6,5,4,3,2,8,1,2,3,10))
print("Minimum Value: ",list(minresult))