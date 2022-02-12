class Person:
    def __init__(self,pid=None,pnm=None,page=None,padr=None):
        self.personId=pid
        self.personName=pnm
        self.personAge=page
        self.personAdr=padr
        self.data={}

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''

    def take_uesr_inputs(self):
        self.data['ID']=int(input("Enter person id: "))
        self.data['Name']=input("Enter your name: ")
        self.data['Age']=int(input("Enter your age: "))
        self.data['Address']=input("Enter your address: ")

        return self.data

    def add_details(self):
        new_data={}
        data=self.take_uesr_inputs()
        new_data[data['ID']]=data
        print("Data Added Successfully")


    def display_details(self):
        if self.data:
            return self.data

if __name__ =="__main__":
    p=Person()

    while True:
        print(" 1 Add\n 2 Display\n 3 Get ID\n 4 Update\n 5 Delete\n 6 Exit")
        choice=int(input("Enter Your Choice "))

        if choice==1:

            print(p.add_details())
        elif choice==2:
            print(p.display_details())
        elif choice==3:
            pass
        elif choice==4:
            pass
        elif choice==5:
            pass
        elif choice==6:
            pass
        else:
            print("Invalid Option.. Try again..")

        choice=input("Do you want to continue :[Y|N]")
        if choice.lower() in ['n','no']:
            break


