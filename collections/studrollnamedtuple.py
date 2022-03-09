from collections import namedtuple

npt=namedtuple('rollnumber',["pandit",'bali','Ajay','ravi'])

n=npt(10,20,30,40)

print("Pandit",n.pandit)

print("Bali",n.bali)

print("Ajay",n.Ajay)

print("Ravi",n.ravi)