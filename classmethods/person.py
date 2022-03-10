class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age


    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

    def get_full_name(self):
        return self.lastname,self.firstname

    @classmethod
    def create_person(cls):
        fname=input("Enter first name: ")
        lname=input("Enter last name: ")
        age=int(input("Enter age: "))
        return Person(fname,lname,age)

p=Person('pandit','patil',32)
print(p)
p.create_person()
print(p.get_full_name())
print(p)