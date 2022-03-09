from collections import deque

de=deque(['Red','Green','White'])
print("Original List: ",de)

de.appendleft('Pink')
print("Appended Left: ",de)

de.append('Orange')
print("Adding to the Right:",de)

de.pop()
print("Removing Right: ",de)

de.popleft()
print("Removing from Left: ",de)

de.reverse()
print("Reversing List: ",de)