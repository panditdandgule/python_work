import itertools

#help(itertools.chain)

x=[[1,2],[3,4]]

print(list(itertools.chain(*x)))