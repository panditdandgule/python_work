from collections import deque

delist=deque([10,20,30,40,50])

print(delist)

delist.rotate(2) #[40, 50, 10, 20, 30]
print(delist)

delist.rotate(1) #[30, 40, 50, 10, 20] using last rotate list
print(delist)