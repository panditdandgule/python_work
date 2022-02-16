import sys
from myerror import MyError
from ecominventory.impl import ProductServiceImpl, Product, ValueDivision
from ecominventory.vendorinfo import Vendor


def take_product_input():
    def take_vendor_input():
        """Take input from User and create Vendor Object"""
        try:
            vid = int(input('Enter Vendor Id : '))
            vname = str(input('Enter Vendor Name : '))
            if vname.isdigit() or vname.isspace():
                raise MyError("unaccepted response.. please enter string only")
            vadr = str(input('Enter Vendor Address : '))
            if vadr.isdigit() or len(vadr) < 4:
                raise MyError("unaccepted response.. please enter string only")
        except ValueError:
            print("Please enter integer value.")
        except TypeError as msg:
            print("Letters only please.", msg)
        except MyError as err:
            print(err.msg)
        return Vendor(vid=vid, vnm=vname, vadr=vadr)

    '''Take input from user --> and create product object...'''
    try:
        pid = int(input('Enter Product Id : '))
        pnam = str(input('Enter Product Name : '))
        if pnam.isdigit() or pnam.isspace():
            raise MyError("Unaccepted response. Please enter valid product name")
        pqty = int(input('Enter Product Qty : '))
        prc = float(input('Enter Product Price : '))
        ven = take_vendor_input()
        cat = str(input('Enter Product Category : '))
        if cat.isdigit() or cat.isspace():
            raise MyError("unaccepted response.. please enter string only")
        return Product(pid=pid, pnm=pnam, pric=prc, pqty=pqty, pven=ven, pcat=cat)
    except ValueError:
        print("Value should be number")
    except TypeError as msg:
        print("Letters only please ", msg)
    except MyError as err:
        print(err.msg)
    except:
        print("Please provide valid input")


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
                12 Exit
       
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
        elif choice == 8:
            try:
                pid = int(input("Enter Product Id which one you want to search:"))
                print(prodService.search_by_id(pid))
            except ValueError as v:
                print("Please int value")
        elif choice == 9:
            try:
                ven = input("Enter Vendor Name which vendor you want to search: ")
                if ven.isdigit():
                    raise MyError("Unaccepted response. Please enter valid input")
                print(prodService.search_by_vendor(ven))
            except MyError as err:
                print(err.msg)
        elif choice == 10:
            total = prodService.total_product_price()
            print("Total Price of Product:", total)
        elif choice == 11:
            try:
                pid = int(input("Enter the product id:"))
                prodService.update_product(pid)
            except ValueError as v:
                print("Please enter int value only", v)
        elif choice == 12:
            print("Thanks for using Inventory Application..")
            sys.exit(0)
        else:
            print('Invalid Choice..')

        ch = str(input('Do you want to continue : Y/N'))
        try:
            if ch.lower() in ['n', 'no']:
                if ch.isdigit() or ch.isspace():
                    raise MyError("Unaccepted response please try again")
                print("Thanks for visit..")
                break
        except MyError as err:
            print(err.msg)
