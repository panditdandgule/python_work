from itertools import tee

v1 = [9,8, 94, 5, 7, 49, 98, 31, 90, 13, 9, 61, 4, 73, 707, 88, 49, 17, 56, 4, 30]


tee = tee(v1,5)

for l in tee:
    print(list(l))