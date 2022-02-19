import sys

from impl import ProductImpl,Product
import logging
logging.basicConfig(filename='mylog.log',level=logging.INFO)
logging.info("The new request came")

def take_user_inputs():
    try:
        pid=int(input("Enter product id"))
        pname=input("Enter product name")
        price=float(input("Enter product price"))
        qty=int(input("Enter product quantity"))
        pven=input("Enter product vendor name")
        return Product(pid,pname,price,qty,pven)

    except ValueError as msg:
        logging.exception(msg)

    except:
        print("Invalid input")
    logging.info("The process completed succesfully")

if __name__=='__main__':
    prod=ProductImpl()
    while True:
        option=int(input("Enter 1. Add 2 Display 3 Exit"))

        if option==1:
            details=take_user_inputs()
            prod.add_data_into_json_file(details)
        elif option==2:
            prod.display_data_json_file()
        elif option==3:
            sys.exit()
            break
        else:
            print("Invalid input")

        ch=input("Do you want to continue (yes|no)")
        if ch.lower() in ['n','no']:
            break