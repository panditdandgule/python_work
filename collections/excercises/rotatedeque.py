from collections import deque

de=deque([2, 4, 6, 8, 10])

print("Deque Before Rotation: ",de)

de.rotate(1)
print("Deque After One Positive Rotation: ",de)

de.rotate(2)
print("Deque After Two Positive Rotation: ",de)