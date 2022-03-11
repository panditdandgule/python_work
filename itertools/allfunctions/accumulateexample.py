import operator
from itertools import accumulate

li=[5,4,6,2,3]

final_list=list(accumulate(li,operator.mul))

print(final_list)