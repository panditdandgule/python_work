import sys

from ecommerce.vendor import Vendor
class Product:
    """This is structure of product class holding data and properties"""
    prodCompany = 'PTECH'

    def __init__(self, pid, pnm, pric,pqty ,pven, pcat):
        self.prodId = pid
        self.prodName = pnm
        self.prodPrice = pric
        self.prodQty=pqty
        self.prodVendor = pven
        self.prodCategory = pcat

    def __str__(self):
        return '{}, {}, {}, {},{},{}\n'.format(self.prodId, self.prodName,
                                            self.prodPrice, self.prodQty,self.prodVendor,
                                            self.prodCategory)

    def __repr__(self):
        return str(self)
class Vendor:
    def __init__(self, vid, vnm, vadr):
        self.vendorId = vid
        self.vendorName = vnm
        self.vendorAddr = vadr

    def __str__(self):
        return '{},{},{}\n'.format(self.vendorId, self.vendorName, self.vendorAddr)

    def __repr__(self):
        return str(self)
v1 = Vendor(101,"Flipkart","Bglore")
v2 = Vendor(102,"Amazon","Bglore")

p1 = Product(pid=101,pnm='MObile1',pric=2936.34,pqty=23,pven=v1,pcat="A+")
p2 = Product(pid=1201,pnm='MObile2',pric=2938.34,pqty=223,pven=v2,pcat="A+")
#p3 = Product(pid=1031,pnm='MObile3',pric=2893.34,pqty=253,pven=v1,pcat="C+")
#p4 = Product(pid=1501,pnm='MObile4',pric=6293.34,pqty=2434,pven=v1,pcat="B+")
#p5 = Product(pid=1601,pnm='MObile5',pric=2593.34,pqty=237,pven=v2,pcat="A+")
#p6 = Product(pid=1071,pnm='MObile6',pric=4293.34,pqty=238,pven=v1,pcat="C+")

#productList =[p1,p2,p3,p4,p5,p6]
productList =[p1,p2]
def remove_product():

    if productList:
        userInput=int(input("Please Enter Product Id which one you want to delete?"))
        for prod in productList:
            if userInput==prod.prodId:
                print("The following prod id Deleted successfully: ",prod.prodId)
                print("\n",prod)
                productList.remove(prod)
                break
    else:
        print("No Records in product list")

remove_product()
"""
prodToModify = int(input("Enter the product id:"))
# search for the record to update
for prod in productList:
    if prodToModify == prod.prodId:
            print(prod)
            break
    else:
        print("Record not found")
        break

option = int(input(
    '1. To modify name, 2. To modify price, 3. To modify vendor, 4. To modify catogory 5. To modify vendor name 6. To modify vendor adress: '))
if option == 1:
    prod.prodName= input("Enter to modify:")
    productList.insert(prod.prodId,prod.prodName)
    print(prod)
    print("Updated Product Name Successfully.")
elif option==2:
    prod.prodPrice=float(input(("Enter to modify:")))
    productList.insert(prod.prodId,prod.prodPrice)
    print(prod)
    print("Updated Product Price Successfully")
elif option==3:
    prod.prodVendor=input("Enter to modify:")
    productList.insert(prod.prodId,prod.prodVendor)
    print("Updated Vendor name successfully..")
elif option==4:
    prod.prodCategory=input("Enter to modify")
    productList.insert(prod.prodId,prod.prodCategory)
    print("Updated prod category successfully.")
elif option==5:
    prod.prodVendor=input("Enter to modify:")
    productList.insert(prod.prodId,prod.prodVendor)
    print("Updated Vendor Successfully")
elif option==6:
    v1.vendorAddr=input("Enter to modify:")
    productList.insert(prod.prodId,v1.vendorAddr)
    print(prod)
    print("Updated vendor address successfully")
else:
    print('Incorrect option selected.')
"""