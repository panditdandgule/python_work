import itertools

for i in itertools.count(5,5):
    if i==35:
        print(i)
        break
    else:
        print(i,end=" ")