import sys

from personimpl import PersonServicesImpl,PersonInfo
from personaddress import PersonAddress

def take_user_details():
    """Getting the details from the user to adding the file"""
    def take_user_address():
        city=input("Enter City Name: ")
        state=input("Enter State Name: ")
        country=input("Enter Country Name: ")
        pin=input("Enter Pincode Number: ")
        return PersonAddress(city=city,state=state,country=country,pin=pin)
    try:
        personId=int(input("Enter Id: "))
        personName=input("Enter Name: ")
        personDob=int(input("Enter Date Of Birth: (DDMMYYYY)"))
        personEmail=input("Enter Email: ")
        personPhone=int(input("Enter Mobile Number: "))
        personAdr=take_user_address()
    except ValueError as msg:
        print("Enter only integral numbers only..")
    except KeyboardInterrupt as error:
        raise error
    except:
        print("Please enter valid input..")
    return PersonInfo(pid=personId,pnm=personName,pdob=personDob,pemail=personEmail,pcont=personPhone,padr=personAdr)


if __name__ == '__main__':
    person=PersonServicesImpl()

    while True:
        print("Enter\n 1 Add\n 2 Display\n 3 Search\n 4 Update\n 5 Delete\n 6 Exit ")
        choice=int(input())
        if choice==1:
            persondetails=take_user_details()
            print(person.add_person_details(persondetails))
        elif choice==2:
            print(person.display_all_persons())
        elif choice==3:
            pid=int(input("Enter Person Id to search :"))
            print(person.get_person_details(pid))
        elif choice==4:
            pid=int(input("Enter person id to update: "))
            person.update_person_details(pid)
        elif choice==5:
            pid=int(input("Enter Person Id which one you want to delete?:"))
            person.delete_person_details(pid)
        elif choice==6:
            print("Thanks for using app")
            sys.exit()

        ch = input('Do you want to continue : Y/N')
        if ch.lower() in ['n', 'no']:
            break