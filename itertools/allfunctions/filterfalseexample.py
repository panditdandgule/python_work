"""
Filters elements from iterable returning only those for which the predicate is False.
If predicate is None return the items that are False.
"""
import random
from itertools import filterfalse
#li=[random.randint(1,30) for x in range(20) ]
li=[5,7,22,97,54,62,77,23]
print("Original list: ",li)

final_list=list(filterfalse(lambda x:x%2==0,li))
print("Only False Value printing: ",final_list)
