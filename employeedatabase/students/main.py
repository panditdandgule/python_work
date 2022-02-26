from studinfo import Student
from impl import StudentImpl

def take_user_inputs():
    try:
        studId=int(input("Enter Student Id: "))
        studName=input("Enter student name:")
        studAge=int(input("Enter student age:"))
        studAddr=input("Enter Student Address:")
        return Student(sid=studId,sname=studName,sage=studAge,saddr=studAddr)
    except ValueError as e:
        print("There was an error",e)
    finally:
        pass

if __name__=='__main__':
    stud=StudentImpl()

    #add data to the database
    #details=take_user_inputs()
    #stud.add_student_info(details)

    #display data
    print("All students info..")
    stud.display_student_info()

    #update data
    id=int(input("Enter id which id you want to update? "))
    name=input("Enter name for update : ")
    stud.update_student_info(id,name)