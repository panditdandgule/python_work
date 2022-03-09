from collections import ChainMap
import sys
print(dir(ChainMap))
sys.exit(0)
d1={'a':10,'b':20}
d2={'b':30,'d':40}
d3={'e':50,'f':60}

c=ChainMap(d1,d2,d3)

print(c)

print(c.get('b'))

d0={'e':55,'f':66}

d=c.new_child(d0) #adding new dictionary at the begining of chainmap

print(d.parents) #removed first dictionary in chainmap
print(d.parents)
print(d.parents)
#print(help(d))