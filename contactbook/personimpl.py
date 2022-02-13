import os
import pickle

from personservices import PersonServices, PersonInfo
import sys


class PersonServicesImpl(PersonServices):
    persondetailsList = []
    filename = 'persondetails'

    def add_person_details(self, persondetails):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                myPersonDetails = open(self.filename, 'rb')
                self.persondetailsList = pickle.load(myPersonDetails)
                myPersonDetails.close()
            else:
                myPersonDetails = open(self.filename, 'wb')

            self.persondetailsList.append(persondetails)
            myPersonDetails = open(self.filename, 'wb')
            pickle.dump(self.persondetailsList, myPersonDetails)
            myPersonDetails.close()

            print("Details Added Successfully")
        except:
            print("There was an error! Data was not added.")
        finally:
            myPersonDetails.close()

    def display_all_persons(self):
        allDetails = []
        try:
            if os.path.exists(self.filename) and os.path.exists(self.filename) > 0:
                myPersonDetails = open(self.filename, 'rb')
                listOfDetails = pickle.load(myPersonDetails)
                for listdetl in listOfDetails:
                    allDetails.append(listdetl)
                return allDetails
            else:
                print("File is empty")
        except:
            print("There was an error while displaying details")

    def get_person_details(self, pid):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                myPersonDetails = open(self.filename, 'rb')
                data = pickle.load(myPersonDetails)
                for x in data:
                    if x.personId == pid:
                        return x
                    else:
                        return "Data is not available.."

        except:
            print("There was an error while facing particular id")

    def update_person_details(self, pid):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                myPersonDetails = open(self.filename, 'rb')
                data = pickle.load(myPersonDetails)
                myPersonDetails.close()
                try:
                    for person in data:
                        if person.personId == pid:
                            break
                        else:
                            return False
                except:
                    print("Data is not available..")
                else:
                    print("Enter your choice which one you want to modify:")
                    print("1 Name 2 DOB 3 Email 4 Contact 5 City 6 State 7 Country 8 Pin 9 Exit")
                    while True:
                        choice = int(input())
                        if choice == 1:
                            personName = input("Enter Name:")
                            person.personName(personName)
                            myPersonDetails = open(self.filename, 'wb')
                            pickle.dump(data, myPersonDetails)
                            print("Updated name successully")
                            break
                        elif choice == 2:
                            personDob = int(input("Enter DOB: "))
                            person.personDob(personDob)
                            myPersonDetails = open(self.filename, 'wb')
                            pickle.dump(data, myPersonDetails)
                            print("Updated DOB Successfully..")
                            break
                        elif choice == 3:
                            personEmail = input("Enter person email: ")
                            person.personEmail(personEmail)
                            myPersonDetails = open(self.filename, 'wb')
                            pickle.dump(data, myPersonDetails)
                            print("Updated Email successfully")
                            break
                        elif choice == 4:
                            personCont = int(input("Enter Contact"))
                            person.personCont(personCont)
                            myPersonDetails = open(self.filename, 'wb')
                            pickle.dump(data, myPersonDetails)
                            break
                        else:
                            print("Invalid option")
                            continue





        except:
            print("There was an error while updating data..")

    def delete_person_details(self, pid):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                myPersonDetails = open(self.filename, 'rb')
                data = pickle.load(myPersonDetails)
                myPersonDetails.close()
                for i in range(0, len(data)):
                    each_person = data[i]
                    if each_person.personId == pid:
                        del data[i]
                        print("Deleted successfully")
                        myPersonDetails = open(self.filename, "wb")
                        if (len(data) == 0):
                            myPersonDetails.write("")
                        else:
                            pickle.dump(data, myPersonDetails)
                        break
        except:
            print("There was an error while Deleting particular id..")
