import sys

from implementation import ContactImplementation
from personinfo import Person
from contactinfo import Contact

if __name__ == '__main__':
    per = Person()
    cont = ContactImplementation()

    while True:
        print(
            "Enter Choice:\n 1 Add Contact\n 2 Display Contact\n 3 Search Contact\n 4 Update Contact\n 5 Delete Contact\n 6 Exit")
        choice = int(input())
        if choice == 1:
            userInputs = per.get_user_details()
            print(cont.add_contact(userInputs))
        elif choice == 2:
            print(cont.display_contacts())
        elif choice == 3:
            pname = input("Enter Person Name which one you want to search? ").upper()
            print(cont.search_contact(pname))
        elif choice == 4:
            pname = input("Enter Person Name which one you want to update? ").upper()
            cont.update_contact(pname)
        elif choice == 5:
            pname = input("Enter Person Name which one you want to delete? ").upper()
            cont.delete_contact(pname)
        elif choice == 6:
            print("Thanks for using application..")
            sys.exit()

        ch = input("Do you want to continue (Y|N) ")
        if ch.lower() in ['n', 'no']:
            print("Thanks for visit..")
            break
