from collections import deque

nums = (2,9,0,8,2,4,0,9,2,4,8,2,0,4,2,3,4,4,4,4,4,4,0)
nums_dq=deque(nums)
print("Number of twos: ",nums_dq.count(2))

print("Number of Fours: ",nums_dq.count(4))