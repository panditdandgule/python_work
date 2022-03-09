from collections import Counter

c1=Counter([1,2,3,4,5])
c2=Counter([4,5,6,7,8])

print("C1:",c1)
print("C2:",c2)

c=c1+c2
print("Combined Count: ",Counter(c))

c1.subtract(c2)
print(c1)

