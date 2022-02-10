import sys
from product import Product
from vendor import Vendor

"""
This is the main class for performing below operations.
add_product         : Taking inputs through user and adding products.
search_product      : Searching product using product name
update_product      : Updating product
remove_product      : Deleting product using product id
get_product         :  Getting particular product
display_all_product : Displaying all products
average_product     : Calculating Average Price
sum_of_product      : Total products
min_of_product      : Minimum Price of Product
max_of_product      : Maximum Price Of Product
search_vendor       : Searching vendor by name
search_category     : Searching category by using category
"""


def add_product():
    """Taking user inputs(Product and Vendor Details)"""

    def take_vendor_input():
        vid = int(input("Enter vendor id:"))
        vname = input("Enter vendor name:")
        vadr = input("Enter vendor address:")
        return Vendor(vid, vname, vadr)

    pid = int(input("Enter product id: "))
    pnm = input("Enter product name:")
    pric = float(input("Enter product price:"))
    pqty = int(input('Enter Product Qty : '))
    pven = take_vendor_input()
    pcat = input("Enter product category:")
    return Product(pid, pnm, pric, pqty, pven, pcat)


def search_product(pnm):
    prodlist = []
    for prod in productList:
        if prod.prodName == pnm:
            prodlist.append(prod)

    return prodlist


def update_product():
    prodToModify = int(input("Enter the product id:"))

    # search for the record to update
    for prod in productList:
        if prodToModify == prod.prodId:
            break
        else:
            print("Record not found")
            break

    option = int(input(
        '1. To modify name, 2. To modify price, '
        '3. To modify vendor, ''4. To modify category '
        '5. To modify vendor name ''6. To modify vendor adress: '))
    if option == 1:
        prod.prodName = input("Enter to modify product name :")
        productList.insert(prod.prodId, prod.prodName)
        print(prod)
        print("Updated Product Name Successfully.")
    elif option == 2:
        prod.prodPrice = float(input(("Enter to modify product price:")))
        productList.insert(prod.prodId, prod.prodPrice)
        print(prod)
        print("Updated Product Price Successfully")
    elif option == 3:
        prod.prodVendor = input("Enter to modify product vendor:")
        productList.insert(prod.prodId, prod.prodVendor)
        print(prod)
        print("Updated Vendor name successfully..")
    elif option == 4:
        prod.prodCategory = input("Enter to modify product catogory")
        productList.insert(prod.prodId, prod.prodCategory)
        print(prod)
        print("Updated prod category successfully.")
    elif option == 5:
        prod.prodVendor = input("Enter to modify product vendor:")
        productList.insert(prod.prodId, prod.prodVendor)
        print(prod)
        print("Updated Vendor Successfully")
    elif option == 6:
        prod.vendorAddr = input("Enter to modify vendor Address:")
        productList.insert(prod.prodId, prod.vendorAddr)
        print(prod)
        print("Updated vendor address successfully")
    else:
        print('Incorrect option selected.')


def remove_product():
    if productList:
        userInput = int(input("Please Enter Product Id which one you want to delete?"))
        for prod in productList:
            if userInput == prod.prodId:
                print("The following prod id Deleted successfully: ", prod.prodId)
                print("\n", prod)
                productList.remove(prod)
                break
    else:
        print("No Records in product list")


def get_product():
    prodToSearch = input("Enter product name:")
    counter = 0
    for prod in productList:
        if prodToSearch == prod.prodName:
            print(prod)
            counter += 1
    if counter == 0:
        print("No record found whose name is:", prodToSearch)


def display_all_product():
    if productList:
        for product in productList:
            print(product)
    else:
        print("No record in product list..")


def average_product():
    total = 0
    for price in productList:
        if price.prodPrice:
            total += price.prodPrice

    avg = total / len(productList)
    print("Average of product:", avg)


def sum_of_product():
    print("Number of product list: ", len(productList))


def min_of_product():
    min_value = None
    for price in productList:
        if price.prodPrice:
            if (min_value is None or price.prodPrice > min_value):
                min_value = price.prodPrice
                print(price)

    print('Minumum Product Price Value:', min_value)


def max_of_product():
    max_value = None
    for price in productList:
        if price.prodPrice:
            if (max_value is None or price.prodPrice > max_value):
                max_value = price.prodPrice
                print(price)

    print('Maximum Product Price Value:', max_value)


def search_vendor(vendorName):
    venProdList = []
    for prod in productList:
        if prod.prodVendor.vendorName == vendorName:
            venProdList.append(prod)
    return venProdList


def search_category(pcat):
    prodCatogory = []
    for ven in productList:
        if pcat == ven.prodCategory:
            prodCatogory.append(ven)

    return prodCatogory


if __name__ == '__main__':
    print("Welcome to ", Product.prodCompany)
    print()
    print(
        'Enter :\n 1. To Add Product\n 2. To Searching a Product\n 3. To Update a Product\n 4. To Get Product\n 5. To '
        'Display All Product\n 6. To Average Product Price\n '
        '7. To Sum Of Product\n 8. To Min Of Product\n 9. To Max Of Product\n 10.To Search By Vendor\n 11.To Search '
        'By Category\n 12.To Remove Product\n 13.To Exit')
    productList = []

    while True:
        choice = int(input('Enter Your Choice(Choice should be integer number):'))

        if choice == 1:
            product = add_product()
            productList.append(product)

        elif choice == 2:
            pnm = input("Enter product name:")
            print(search_product(pnm))
        elif choice == 3:
            update_product()
        elif choice == 4:
            get_product()
        elif choice == 5:
            display_all_product()
        elif choice == 6:
            average_product()
        elif choice == 7:
            sum_of_product()
        elif choice == 8:
            min_of_product()
        elif choice == 9:
            max_of_product()
        elif choice == 10:
            vendorName = input("Enter vendor name:")
            print(search_vendor(vendorName))
        elif choice == 11:
            pcat = input("Enter product category name: ")
            print(search_category(pcat))
        elif choice == 12:
            remove_product()
        elif choice == 13:
            print("Thanks For Using Ecommerce Application.")
            sys.exit(0)
        else:
            print("Invalid Option Please Try Again..")
