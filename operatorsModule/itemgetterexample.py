from operator import itemgetter

x=[(1,10),(-1,11),(2,110),(0,-1)]

print("Original Elements: ",x)

print("Using Lambda: ",sorted(x,key=lambda x:x[1]))

print("Using Itemgetter: ",sorted(x,key=itemgetter(1)))

#If some elements duplicates
x=[(1,10),(-1,11),(2,110),(2,-1),(0,-1)]

print("Using Lambda: ",sorted(x,key=lambda x:(x[1],x[0])))

print("Using Itemgetter: ",sorted(x,key=itemgetter(1,0)))