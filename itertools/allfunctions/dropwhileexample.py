from itertools import dropwhile

li=[1,4,6,4,1]

final_list=list(dropwhile(lambda x:x<5,li))

print(final_list)