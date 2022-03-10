from itertools import chain

chain_func=([1, 2, 3], ['a', 'b', 'c', 'd'], [4, 5, 6, 7, 8])

result=chain(*chain_func)

print(list(result))
