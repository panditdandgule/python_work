from collections import Counter

items=['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']

contr=Counter(items)
print(contr)
print(Counter(items).most_common(1)[0][0])