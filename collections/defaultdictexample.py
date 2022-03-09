from collections import defaultdict

val1=defaultdict(int)

for i in range(5):
    val1[i]=i

print(val1)

if val1[5]==500:
    print("hello")
else:
    print("No")