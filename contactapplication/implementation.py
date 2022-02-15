import sys
from services import ContactServices
from personinfo import Person


class ContactImplementation(ContactServices):
    contactList = []

    def add_contact(self, userInputs):
        try:
            if type(userInputs) == Person:
                record = self.search_contact(userInputs.firstName)
                if record in ContactImplementation.contactList:
                    return "The Contact Already Available"
                    sys.exit()
                else:
                    ContactImplementation.contactList.append(userInputs)
                    print("Contact added successfully.")
                    return ContactImplementation.contactList
            else:
                print("Invalid details")
        except:
            print("There was an error..! Data was not added.")

    def display_contacts(self):
        newList = []
        try:
            if ContactImplementation.contactList:
                for person in ContactImplementation.contactList:
                    newList.append(person)
            else:
                print("Person List is empty..")
            return newList
        except:
            print("Something went wrong while displaying..")

    def search_contact(self, pname):
        try:
            if ContactImplementation.contactList:
                for person in ContactImplementation.contactList:
                    if person.firstName == pname:
                        return person
                    else:
                        return "No record in list"
            else:
                print("Person List is empty..")
        except:
            print("Something went wrong while searching..")

    def update_contact(self, pname):
        try:
            if ContactImplementation.contactList:
                for person in ContactImplementation.contactList:
                    if pname == person.firstName:
                        break
                    else:
                        print("No Record found for update..")
                        return False

                try:
                    print("Choose Option\n 1 Title 2 FIRSTNAME 3 LASTNAME 4 GENDER 5 DOB\n"
                          " 6 PHONE 7 STREET 8 CITY 9 STATE 10 COUNTRY 11 PINCODE")

                    option = int(input("Enter your choice: "))
                except ValueError:
                    print("Choose only integer value")
                else:
                    if option == 1:
                        person.pTitle = input("Enter Title: ").title()
                        ContactImplementation.contactList.insert(person.firstName, person.pTitle)
                        print("Person Title Updated Successfully..")
                    elif option == 2:
                        person.firstName = input("Enter First Name: ").upper()
                        ContactImplementation.contactList.insert(person.firstName, person.firstName)
                        print("Person First Name Updated Successfully..")
                    elif option == 3:
                        person.lastName = input("Enter Last Name: ")
                        ContactImplementation.contactList.insert(person.firstName, person.lastName)
                        print("Person Last Name Updated Successfully..")
                    elif option == 4:
                        person.pGender = input("Enter Gender: ")
                        ContactImplementation.contactList.insert(person.firstName, person.pGender)
                        print("Person Gender Updated Successfully..")
                    elif option == 5:
                        person.pDob = int(input("Enter DOB: "))
                        ContactImplementation.contactList.insert(person.firstName, person.pDob)
                        print("Person DOB updated Successfully..")
                    elif option == 6:
                        person.pPhone = int(input("Enter Phone: "))
                        ContactImplementation.contactList.insert(person.firstName, person.pPhone)
                        print("Person Phone updated Successfully..")
                    elif option == 7:
                        person.contStreet = input("Enter Street: ")
                        ContactImplementation.contactList.insert(person.firstName, person.contStreet)
                        print("Person Street Updated Successfully..")
                    elif option == 8:
                        person.contCity = input("Enter City: ")
                        ContactImplementation.contactList.insert(person.firstName, person.contCity)
                        print("Person City Updated Successfully..")
                    elif option == 9:
                        person.contState = input("Enter State: ")
                        ContactImplementation.contactList.insert(person.firstName, person.contState)
                        print("Person State Updated Successfully..")
                    elif option == 10:
                        person.contCountry = input("Enter Country: ")
                        ContactImplementation.contactList.insert(person.firstName, person.contCountry)
                        print("Person Country Updated Successfully..")
                    elif option == 11:
                        person.conPincode = int(input("Enter Pincode: "))
                        ContactImplementation.contactList.insert(person.firstName, person.conPincode)
                        print("Person Pincode updated Successfully..")
                    else:
                        print("Please Enter valid input")


            else:
                print("The list is empty..")
        except:
            print("There was an error..! While updating data")

    def delete_contact(self, pname):
        try:
            if ContactImplementation.contactList:
                for person in ContactImplementation.contactList:
                    record = self.search_contact(pname)
                    if record:
                        ContactImplementation.contactList.remove(person)
                        print("Contact Successfully Deleted..")
                    else:
                        return "No record found for delete.."
            else:
                print("List Is Empty..")

        except:
            print("Something went wrong while deleting contact..")
