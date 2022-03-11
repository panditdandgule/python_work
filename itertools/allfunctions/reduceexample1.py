from functools import reduce

li=[10,20,30,40]

final_list=reduce(lambda x,y:x+y,li)

print(final_list)