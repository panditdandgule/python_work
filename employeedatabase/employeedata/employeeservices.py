from abc import ABC, abstractmethod
from empinfo import Employee


class EmployeeServices(ABC):

    @abstractmethod
    def add_employee_details(self):
        pass

    @abstractmethod
    def display_employee_details(self):
        pass

    @abstractmethod
    def search_employee_details(self):
        pass

    @abstractmethod
    def update_employee_details(self):
        pass

    @abstractmethod
    def delete_employee_details(self):
        pass
