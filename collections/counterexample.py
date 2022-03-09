from collections import Counter

elements=[19,6,23,18,28,22,13,23]

contr=Counter(elements)

print(contr)

print(contr.most_common())

vallist=contr.elements()
print(list(vallist))