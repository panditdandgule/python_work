from collections import deque

de=deque([1,2,3,4])

print(de)

#Elements can be insert both sides
de.append(5) #appending right
print(de)

de.appendleft(0) #appending left
print(de)

#Elements can be remove both sides
de.pop() #elments remove right
print(de)
de.popleft() #elements remove from left
print(de)

