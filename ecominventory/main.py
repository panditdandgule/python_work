import sys
import logging
from myerror import MyError
from ecominventory.impl import ProductServiceImpl, Product, ValueDivision
from ecominventory.vendorinfo import Vendor

logging.basicConfig(filename='mylog.txt',level=logging.INFO)
logging.info("A new request came")

def take_product_input():
    def take_vendor_input():
        """Take input from User and create Vendor Object"""
        try:
            vid = int(input('Enter Vendor Id : '))
            vname = str(input('Enter Vendor Name : ')).title()
            if vname.isdigit() or vname.isspace():
                raise MyError("unaccepted response.. please enter string only")
            vadr = str(input('Enter Vendor Address : ')).title()
            if vadr.isdigit() or len(vadr) < 4:
                raise MyError("unaccepted response.. please enter string only")
        except ValueError:
            print("Please enter integer value.")
        except TypeError as msg:
            print("Letters only please.", msg)
        except MyError as err:
            print(err.msg)
        logging.exception(err.msg)
        return Vendor(vid=vid, vnm=vname, vadr=vadr)

    '''Take input from user --> and create product object...'''
    try:
        pid = int(input('Enter Product Id : '))
        pnam = str(input('Enter Product Name : ')).title()
        if pnam.isdigit() or pnam.isspace():
            raise MyError("Unaccepted response. Please enter valid product name")
        pqty = int(input('Enter Product Qty : '))
        prc = float(input('Enter Product Price : '))
        ven = take_vendor_input()
        cat = str(input('Enter Product Category : ')).upper()
        if cat.isdigit() or cat.isspace():
            raise MyError("unaccepted response.. please enter string only")
        return Product(pid=pid, pnm=pnam, pric=prc, pqty=pqty, pven=ven, pcat=cat)
    except ValueError as msg:
        print("Value should be number")
        logging.exception(msg)
    except TypeError as msg:
        print("Letters only please ", msg)
    except MyError as err:
        print(err.msg)
    except:
        print("Please provide valid input")
    logging.info("Request processing completed")


if __name__ == '__main__':
    prodService = ProductServiceImpl(ValueDivision)
    while True:
        print('''
                1 Add_product
                2 Avg_product_price
                3 Delete_product
                4 Get_all_product
                5 Min_product_price
                6 Max_product_price
                7 Search_by_category
                8 Search_by_id
                9 Search_by_vendor
                10 Total_product_price
                11 Update_product
                12 Product Names
                13 Product Quantity
                14 Display All Product Quantity
                15 Withdraw Product Quantity
                16 All Product Category List
                17 All Vendors List
                18 All Products List By Vendor
                19 Display Vendor Address
                20 Exit
       
        ''')
        try:
            choice = int(input('Enter Your Choice : '))
        except ValueError:
            print("Enter Valid Choice. Please Try again..")
            continue
        if choice == 1:
            product = take_product_input()
            prodService.add_product(product)
        elif choice == 2:
            avg = prodService.avg_product_price()
            print('Total Product Price : ', avg)
        elif choice == 3:
            try:
                pid = int(input("Enter product id to delete? "))
                print(prodService.delete_product(pid))
            except ValueError as v:
                print("Please enter valid product id")
                continue

        elif choice == 4:
            prodList = prodService.get_all_product()
            print('Products', prodList)
        elif choice == 5:
            prodService.min_product_price()
        elif choice == 6:
            prodService.max_product_price()
        elif choice == 7:
            try:
                cat = input("Enter category which one you want to search?")
                if cat.isdigit():
                    raise MyError("Unaccepted response enter valid input")
                print(prodService.search_by_category(cat))
            except MyError as err:
                print(err.msg)
                continue
        elif choice == 8:
            try:
                pid = int(input("Enter Product Id which one you want to search:"))
                print(prodService.search_by_id(pid))
            except ValueError as v:
                print("Please int value")
                continue
        elif choice == 9:
            try:
                ven = input("Enter Vendor Name which vendor you want to search: ")
                if ven.isdigit():
                    raise MyError("Unaccepted response. Please enter valid input")
                print(prodService.search_by_vendor(ven))
            except MyError as err:
                print(err.msg)
                continue
        elif choice == 10:
            total = prodService.total_product_price()
            print("Total Price of Product:", total)
        elif choice == 11:
            try:
                pid = int(input("Enter the product id:"))
                prodService.update_product(pid)
            except ValueError as v:
                print("Please enter int value only", v)
                continue
        elif choice == 12:

            print(prodService.product_names())
        elif choice == 13:
            pname = input("Enter product name: ")
            print(prodService.product_quantity(pname))
        elif choice == 14:
            print(prodService.display_all_product_quantity())
        elif choice == 15:
            pname = input("Please enter which product you want to buy..")
            prodService.withdraw_product_quantity(pname)
        elif choice == 16:
            print("All Product Category List: ")
            print(prodService.all_product_category_list())
        elif choice == 17:
            print("All Vendor Name List:")
            print(prodService.all_vendors_list())
        elif choice == 18:
            vname = input("Enter Vendor Name which one want to see products: ").title()
            print("All Products with Vendor Names")
            print(prodService.all_products_by_vendor(vname))
        elif choice == 19:
            vname = input("Enter Vendor Name:").title()
            print(prodService.display_vendor_address(vname))
        elif choice == 20:
            print("Thanks for using Inventory Application..")
            sys.exit(0)
        else:
            print('Invalid Choice..')

        ch = str(input('Do you want to continue : Y/N'))
        try:
            if ch.lower() in ['n', 'no']:
                if ch.isdigit() or ch.isspace():
                    raise MyError("Unaccepted response please try again")
                    continue
                print("Thanks for visit..")
                break
        except MyError as err:
            print(err.msg)
