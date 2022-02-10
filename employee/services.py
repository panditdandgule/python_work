from abc import ABC,abstractmethod

class EmployeeServices(ABC):

    @abstractmethod
    def add_employee(self):
        pass

    @abstractmethod
    def display_all_employee(self):
        pass

    @abstractmethod
    def get_employee(self,empid):
        pass

    @abstractmethod
    def update_employee(self,empid):
        pass

    @abstractmethod
    def delete_employee(self,empid):
        pass