from impl import StudentImpl, Student

import logging

logging.basicConfig(filename='mylog.txt', level=logging.INFO)
logging.info("A New request came")


def get_stud_inputs():
    try:
        studId = int(input("Enter Student Id: "))
        studName = input("Enter Student Name: ")
        studAge = int(input("Enter Student Age: "))
        studAdr = input("Enter Studetn Address: ")
        return Student(studId, studName, studAge, studAdr)
    except ValueError as msg:
        logging.exception(msg)
    except:
        print("Enter Valid input..")
    logging.info("Process completed successfully..")


if __name__ == '__main__':
    stud = StudentImpl()

    while True:
        option = int(input("Enter 1 Add Data 2 Read Data"))

        if option == 1:
            studdetails = get_stud_inputs()
            stud.add_student_info(studdetails)
        elif option == 2:
            stud.read_student_info()
        else:
            print("Invalid option")

        ch = input("Do you want to continue(yes|no)..")
        if ch.lower() in ['n', 'no']:
            break
