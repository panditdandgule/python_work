import pickle

class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def display(self):
        print("Employee No:",self.eno)
        print("Employee Name:",self.ename)
        print("Employee salary:",self.esal)
        print("Employee Address:",self.eaddr)

with open('emp.dat','wb') as f:
    e=Employee(1,'pandit',100000,'Pune')
    pickle.dump(e,f)
    print("Pickling of employee oject competed")

with open('emp.dat','rb') as f:
    obj=pickle.load(f)
    print("Printing the Employee information after unpikling")
    obj.display()