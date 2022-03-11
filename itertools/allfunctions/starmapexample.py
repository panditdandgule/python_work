from itertools import starmap

val1=[(3,2),(4,5),(6,8),(9,2)]
final_list=list(starmap(lambda x,y:x+y,val1))
print(final_list)

val2=[(4,3,5),(3,2,6),(7,9,10),(5,2,4)]
final_result=list(starmap(lambda x,y,z:x+y+z,val2))
print(final_result)

val3=[(2,3,4,5),(9,2,3,2),(6,2,3,4),(4,2,4,3)]
final=list(starmap(lambda a,b,c,d:a+b+c+d,val3))
print(final)