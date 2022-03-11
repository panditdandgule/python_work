"""
map function returns list of results after applying given function to each item of given iterable.
"""

li=[10,20,30,40]

def addition(n):
    return n+n

result=list(map(addition,li))

print(result)