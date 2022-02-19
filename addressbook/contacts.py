import json
import sys
import logging
logging.basicConfig(filename='mylog.log',level=logging.INFO)
logging.info("The new request came")

class ContactInfo:
    def __init__(self,name=None,address=None,email=None,phone=None):
        self.name=name
        self.address=address
        self.email=email
        self.phone=phone
        self.filename='addressbook'
        self.contacts={}

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n{self.__dict__}\n'''


    def get_user_inputs(self):
        try:
            self.contacts['Name'] = str(input('Enter Contact\'s Full Name: '))
            self.contacts['Address'] = str(input('Enter Contact\'s Address: '))
            self.contacts['Email'] = str(input('Enter Contact\'s Email Address: '))
            self.contacts['Phone'] = int(input('Enter Contact\'s Phone Number: '))
            return self.contacts

        except ValueError as msg:
            logging.exception(msg)
        except:
            print("Invalid input")

    def add_contact_details(self):
        data={}
        contact=self.get_user_inputs()
        data[contact['Name']]=contact

        with open(self.filename,'w') as f:
            json.dump(data,f)
            print("Contact added successfully")

    def display_contact_details(self):
        with open(self.filename,'r') as f:
            data=json.load(f)

        for cont in data.values():
                print(cont)

    def search_contact_details(self):
        with open(self.filename,'r') as f:
            data=json.load(f)
        contactToSearch = input('Enter the name of the contact to search: ')
        counter = 0
        if data:
            for record in data.values():
                if contactToSearch in record['Name']:
                    print(data[record['Name']])
                    counter += 1
                if counter == 0:
                    print('No record found whose name is:', contactToSearch)
#cont=ContactInfo()
#cont.add_contact_details()
#cont.display_contact_details()
#cont.search_contact_details()

