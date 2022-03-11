from itertools import accumulate

li=[1,2,3,4,5,6]

final_list=list(accumulate(li,func=lambda x,y:x*y))

print(final_list)