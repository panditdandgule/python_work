from collections import namedtuple

npt=namedtuple('marks',['Physics','Maths','English'])

m=npt(89,98,100)

print(m.Physics)

print(m.Maths)

print(m.English)