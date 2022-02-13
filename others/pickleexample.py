import os
import pickle

filename='newfile'

data=[10,20,30,40]

def adding_details():
    if os.path.exists(filename) and os.path.getsize(filename)>0:
        myfile=open(filename,'rb')
        data1=pickle.load(myfile)
        myfile.close()

    else:
        myfile=open(filename,'wb')

    data.append(50)
    myfile=open(filename,'wb')
    pickle.dump(data,myfile)
    myfile.close()

adding_details()