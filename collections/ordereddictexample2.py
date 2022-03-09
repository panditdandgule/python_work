from collections import OrderedDict

val={'A':1111,'C':2222,'B':3333,'D':4444}

val2=OrderedDict(val)
print(val)
val2.move_to_end('A')
print(val2)

val2.move_to_end('A',False)
print(val2)