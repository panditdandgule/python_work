class Student:
    count=0
    def __init__(self,stid,stnm,stag):
        self.studId=stid
        self.studName=stnm
        self.set_age(stag)
        Student.count+=1

        if stag<=0:
            print("Invalid Age")
        else:
            self.stud_age=stag

    def display_student(self):
        print("Total Student %d"%Student.count)
    def __str__(self):
        return f'''ID:{self.studId},Name:{self.studName},Age:{self.stud_age}'''

    def __repr__(self):
        return str(self)

    def get_age(self):
        if self.__dict__.__contains__('_stud_age'):
            return self._stud_age
        return ""

    def set_age(self,age):
        if type(age)==int:
            if age<=0:
                print("Invalid Age..")
            else:
                self._stud_age=age

        else:
            print("Invalid Data...for age")

    stud_age=property(fget=get_age,fset=set_age)

s1=Student(101,'Pandit',-29)
print(s1)
s1.stud_age=49
print(s1)
s1.display_student()