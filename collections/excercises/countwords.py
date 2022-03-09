import operator
from collections import Counter
from collections import OrderedDict

words=[]
n=int(input("Enter number of words: "))

for word in range(5):
    words.append(input().strip())

print(len(words))
c=Counter(words)
print(c.values())


