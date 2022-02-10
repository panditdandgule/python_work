import sys

from collegeassignment.addressinfo import Address
from services import EmployeeServices
from employeeinfo import Employee


def take_user_inputs():
    def take_emp_address():
        try:
            city = input("Enter City Name:")
            state = input("Enter State Name:")
            country = input("Enter Country Name:")
        except TypeError as msg:
            print("Please Enter Valid Input", msg)
        return Address(city, state, country)

    try:
        empid = int(input("Enter Employee Id: "))
        empName = input("Enter Employee Name: ")
        if empName == empName.isdigit() or empName.isspace():
            raise "Unaccepted response"
        empAge = int(input("Enter Employee Age: "))
        empSalary = float(input("Enter Employee Salary: "))
        empAdr = take_emp_address()
    except ValueError as msg:
        print("Enter int value only..", msg)
    except:
        print("Please enter valid input.")
    return Employee(empid, empName, empAge, empSalary, empAdr)


class EmployeeServicesImpl(EmployeeServices):
    employeeList = []

    def add_employee(self):
        try:
            inputs = take_user_inputs()
            if inputs.empId > 0:
                result = self.get_employee(inputs.empId)
                if result:
                    print("Id already available")
                    sys.exit()
                else:
                    EmployeeServicesImpl.employeeList.append(inputs)
                    print("Added Successfully")
                    return EmployeeServicesImpl.employeeList
            else:
                print("Employee id should not be zero..")
        except:
            print("Something went wrong.. Data was not added")

    def display_all_employee(self):
        if EmployeeServicesImpl.employeeList:
            return EmployeeServicesImpl.employeeList

    def get_employee(self, empid):
        if EmployeeServicesImpl.employeeList:
            for emp in EmployeeServicesImpl.employeeList:
                if emp.empId == empid:
                    return emp

    def update_employee(self, empid):
        if EmployeeServicesImpl.employeeList:
            for emp in EmployeeServicesImpl.employeeList:
                if emp.empId == empid:
                    break
                else:
                    print("Record Not found.")
                    return False
            print(" 1 To Modify Name\n 2 To Modify Age\n 3 To Modify Salary\n 4 To Modify Address\n 5 Exit")

            try:
                option = int(input("Choose your option"))
            except:
                print("Please choose valid option")
            else:
                if option == 1:
                    emp.empName = input("Enter Employee Name:")
                    EmployeeServicesImpl.employeeList.insert(emp.empId, emp.empName)
                    print("Employee name updated successfully..")
                elif option == 2:
                    emp.empAge = int(input("Enter Employee Age:"))
                    EmployeeServicesImpl.employeeList.insert(emp.empId, emp.empAge)
                    print("Updated Age successfully")
                elif option == 3:
                    emp.empSalary = float(input("Enter Employee Salary: "))
                    EmployeeServicesImpl.employeeList.insert(emp.empId, emp.empSalary)
                    print("Updated Salary Successfully.")
                elif option == 4:
                    emp.empAdr = input("Enter Employee Address")
                    EmployeeServicesImpl.employeeList.insert(emp.empId, emp.empAdr)
                    print("Updated Address Successfully")
                elif option == 5:
                    sys.exit()
                else:
                    print("Invalid option")

    def delete_employee(self, empid):
        if EmployeeServicesImpl.employeeList:
            for emp in EmployeeServicesImpl.employeeList:
                if emp.empId == empid:
                    EmployeeServicesImpl.employeeList.remove(emp)
                    print("Successfully Deleted..")
