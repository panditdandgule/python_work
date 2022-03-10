class Student:
    counter=0

    def __init__(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.counter=Student.create_stdent()

    @classmethod
    def create_stdent(cls):
        cls.counter=cls.counter+1
        return cls.counter

    def display_student(self):
        return f'''{self.__dict__}'''

s=Student(1,'abc','xyz',32)
print(s.display_student())
s1=Student(2,'pqr','nys',30)
print(s1.display_student())