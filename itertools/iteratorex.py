import operator
import time

#Defining lists
L1=[1,2,3]
L2=[2,3,4]

start=time.time()

#Calculating result
a,b,c=map(operator.mul,L1,L2)

end=time.time()

#Time taken by map function
print("Result:",a,b,c)
print("Time taken by map function:",end-start)

for i in range(3):
    print(L1[i]*L2[i],end=" ")