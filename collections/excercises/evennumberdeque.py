from collections import deque

de=deque([2,4,6,8,10])
print(de)

for i in range(12,21):
    if i%2==0:
        de.append(i)
print(de)