from collections import deque

de=deque([1, 3, 5, 7, 9])
x=len(de)
print("Deque Length: ",x)

for item in range(x):
    de.pop()

print("Deque object after removing all elements: ",de)
print("Deque Length: ",len(de))