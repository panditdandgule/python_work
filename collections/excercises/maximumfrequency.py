"""
output
(2, 5)
"""
from collections import Counter

nums=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]

contr=Counter(nums)

print(contr.most_common(1)[0])