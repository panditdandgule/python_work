from collections import Counter
elements = [19, 6, 23, 18, 28, 22, 28, 21, 15, 12, 23, 4, 21, 14, 12, 6, 13, 15, 19, 12, 18, 1, 23, 10, 20, 28, 6, 13, 20, 27, 30, 12, 30, 13, 2, 7, 11, 17, 4, 16, 30, 21, 9, 30, 7, 4, 13, 28, 13, 12, 21, 27, 9, 26, 8, 30, 6, 2, 17, 23, 7, 5, 14, 27, 7, 20, 15, 29, 17, 30, 13, 29, 16, 1, 21, 14, 16, 6, 23, 23, 6, 18, 1, 18, 25, 23, 22, 27, 1, 5, 10, 20, 8, 10, 21, 16, 20, 11, 5, 28]
#[random.randint(1,30) for item in range(100)] # generate random 100 num, between 1-30

contr = Counter(elements)  #Counter -- is a wrapper of dict--> dict methods + additional methods
print(contr)
val = contr.elements()
print("Most Common Higest Elements: ",contr.most_common(2))
print(list(val))

help(contr)
