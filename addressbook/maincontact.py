from contacts import  ContactInfo

if __name__ == '__main__':
    cont = ContactInfo()
    print('Enter 1. To Add Contacts 2. For Searching a Contact 3. For Modifying a Contact 4. To Display Contacts 5. To Exit')
    while True:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            cont.add_contact_details()
        elif choice == 2:
            cont.display_contact_details()
        elif choice == 3:
            cont.modifyContacts()
        elif choice == 4:
            cont.displayContacts()
        elif choice == 5:
            exit()
        else:
            print('Invalid Option. Try Again!')