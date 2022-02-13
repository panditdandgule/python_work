import pickle
import os

data=[]
filename='xyz'

if os.path.exists(filename) and os.path.getsize(filename)>0:
    myfile=open('xyz','rb')
    newdata=pickle.load(myfile)
    myfile.close()
else:
    myfile=open(filename,'wb')

data.append(range(10))
myfile=open(filename,'wb')
pickle.dump(data,myfile)
myfile.close()

for items in data:
    print(items)