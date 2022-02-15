from contactinfo import Contact
import re


class Person(Contact):
    def __init__(self, title=None, fname=None, lname=None, gender=None, dob=None, email=None, phone=None, street=None,
                 city=None, state=None, country=None, pincode=None):

        self.pTitle = title
        self.firstName = fname
        self.lastName = lname
        self.pGender = gender
        self.pDob = dob
        self.pEmail = email
        self.pPhone = phone
        super(Person, self).__init__(street, city, state, country, pincode)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''

    def get_user_details(self):
        try:

            self.pTitle = input("Enter your title [Mr|Mrs]: ").title()
            self.firstName = input("Enter First Name: ").upper()
            self.lastName = input("Enter Last Name: ").upper()
            self.pGender = input("Enter Gender: ").title()
            self.pDob = int(input("Enter Date Of Birth: "))
            self.pEmail = input("Enter Your Email: ")
            # email=re.findall('\w[a-z._]+@\w[a-z]+\.[a-z]{2,3}',self.pEmail)
            self.pPhone = int(input("Enter Your Phone Number: "))
            self.contStreet = input("Enter Your Street: ").title()
            self.contCity = input("Enter Your City: ").title()
            self.contState = input("Enter Your State: ").title()
            self.contCountry = input("Enter Your Country: ").title()
            self.conPincode = int(input("Enter Your Pincode: "))
            return Person(title=self.pTitle, fname=self.firstName, lname=self.lastName, gender=self.pGender,
                          dob=self.pDob, email=self.pEmail, phone=self.pPhone, street=self.contStreet,
                          city=self.contCity, state=self.contState, country=self.contCountry, pincode=self.conPincode)
        except TypeError:
            print("Please Enter Valid Input..")
        except ValueError:
            print("Please Enter Integer Value..")
        except:
            print("Please Enter Valid Input..")
