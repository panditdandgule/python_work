from itertools import takewhile

li=[1,4,6,4,1]

final_list=list(takewhile(lambda x:x<5,li))

print(final_list)