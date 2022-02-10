import sys
from employeeimpl import EmployeeServicesImpl

if __name__ == '__main__':
    emp = EmployeeServicesImpl()
    while True:
        print("1 Add Employee\n 2 Display All Employee\n 3 Get Employee\n 4 Update Employee\n 5 Delete Employee\n 6 "
              "Exit")
        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError as msg:
            print("Invalid choice.. Please try again.")
        else:
            if choice == 1:
                emp.add_employee()
            elif choice == 2:
                print(emp.display_all_employee())
            elif choice == 3:
                try:
                    empid = int(input("Enter Employee Id:"))
                    print(emp.get_employee(empid))
                except ValueError:
                    print("This is not valid id")
            elif choice == 4:
                try:
                    empid = int(input("Enter Employee id which one you want to update: "))
                    emp.update_employee(empid)
                except:
                    print("This is valid id..")

            elif choice == 5:
                try:
                    empid = int(input("Enter Employee Id which one you want to delete? "))
                    emp.delete_employee(empid)
                except:
                    print("Enter valid id")
            elif choice == 6:
                print("Thanks for using this app..")
                sys.exit()
            else:
                print("Invalid option please try again..")

            option = input("Do you want to continue? [Y|N]")
            if option in ['n', 'no']:
                break
