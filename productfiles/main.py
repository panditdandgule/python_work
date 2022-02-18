import os
import datetime
import stat

from products import Product
from implementation import ProductImplementation
import logging
logging.basicConfig(filename='mylog.txt',level=logging.INFO)
logging.info("A new request came")

def take_user_inputs():
    try:
        pid=int(input("Enter product id: "))
        pname=input("Enter product name:")
        price=float(input("Enter product price"))
        qty=int(input("Enter product quantity: "))
        pven=input("Enter product vendor name:")
        return Product(pid,pname,price,qty,pven)

    except ValueError as msg:
        print(logging.exception(msg))
    except TypeError as msg:
        print(logging.exception(msg))
    except:
        print("Invalid input..")
    logging.info("Request processing completed..")

if __name__ =='__main__':
    prod=ProductImplementation()

    while True:
        option=int(input("Enter 1. Add 2. Write File 3. Read File"))
        if option==1:
            details=take_user_inputs()
            print(prod.add_product(details))
        elif option==2:
            prod.add_data_into_file()
        elif option==3:
            prod.read_data_into_file()
        else:
            print("Invalid option.. Try again..")

        ch=input("Do you want to continue (y|n) :")
        if ch.lower() in ['n','no']:
            break

