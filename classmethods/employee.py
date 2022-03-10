class Employee:
    DEFAULTID="000"
    GRATUTITYAMOUNT=1000000
    def __init__(self,id,name,age,salary,hra):
        self.id=id
        self.name=name
        self.age=age
        self.basic_salary=salary
        self.hra=hra

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

    def total_salary(self):
        return self.basic_salary+self.hra

    @staticmethod
    def compute_gratutity(basic_salary,service):
        amount=basic_salary*service
        if amount>Employee.GRATUTITYAMOUNT:
            return Employee.GRATUTITYAMOUNT
        else:
            amount

    @classmethod
    def create_employee(cls,name,age,salary,hra):
        id=cls.DEFAULTID
        return cls(id,name,age,salary,hra)

if __name__=='__main__':
    e1=Employee(111,'pandit',32,50000,2000)
    print(e1)
    print(e1.total_salary())
    print(e1.compute_gratutity(10000,20))
    print(e1.create_employee('Ravi',33,30000,2000))