from collections import deque

t=(2,4,6)
print(type(t))
print(t)
de=deque(t)
print(type(de))
print(de)

de.append(8)
de.append(10)
de.append(12)
de.appendleft(2)

print(de)
print(type(de))