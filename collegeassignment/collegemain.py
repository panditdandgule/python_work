from studentinfo import Student, Department, Address

studList = []
print("Welcome to", Student.collegeName)

def take_stud_inputs():
    def take_dept_inputs():
        did = int(input("Enter Department Id: "))
        dname = input("Enter Department Name: ")

        return Department(did, dname)


    def take_addr_inputs():
        city = input("Enter City Name: ")
        state = input("Enter State Name: ")
        pincode = input("Enter Pincode: ")
        return Address(city, state, pincode)

    sid = int(input("Enter Student Id: "))
    sname = input("Enter Student Name: ")
    sage = int(input("Enter Student Age: "))
    semail = input("Enter Student Email: ")
    dept = take_dept_inputs()
    addr = take_addr_inputs()

    return Student(sid, sname, sage, semail, dept, addr)





while True:
    stud = take_stud_inputs()
    studList.append(stud)
    choice = input("Enter your choice [Y|N]:")
    if choice.lower() in ['n', 'no']:
        break

print(studList)
