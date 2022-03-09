from collections import ChainMap
x={'R': 'Red', 'B': 'Black', 'P': 'Pink','W':'White'}
y={'G': 'Green', 'W': 'White'}
z={'W':'White','Y':'Yellow'}

newdict=ChainMap(x,y,z)
print("Merged Dictionary: ",newdict)


