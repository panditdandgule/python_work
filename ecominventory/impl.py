import sys
from ecominventory.services import ProductServices
from ecominventory.productinfo import Product


class ProductServiceImpl(ProductServices):
    productList = []  # class level var --> ProductServiceImpl.productList

    def add_product(self, prod: Product):  # instance
        try:
            if type(prod) == Product:  # prod --> XXX : str --> validation --fail
                if prod.prodId > 0:
                    if prod.prodPrice >= 100.0:

                        result = self.search_by_id(prod.prodId)  # Product or None
                        if result:
                            print('Product id already available')
                            sys.exit()
                        else:
                            ProductServiceImpl.productList.append(prod)  # product will be added inside list-->
                            print('Product Added Successfully...')
                    else:
                        print('Invalid Product ProductPrice')
                else:
                    print('Invalid Product Id')
            else:
                print('Invalid Product Type....Product Cannot be added..')
        except:
            print("There was error product was not added.")

    def avg_product_price(self):
        avgPrice = 0.0
        if ProductServiceImpl.productList:
            try:
                totalProductPrice = self.total_product_price()
                avgPrice = totalProductPrice / len(ProductServiceImpl.productList)
                return avgPrice
            except:
                print("There was an error while calculating average..")
        else:
            return avgPrice

    def delete_product(self, pid: int):
        try:
            if ProductServiceImpl.productList:
                deleteList = []
                for prod in ProductServiceImpl.productList:
                    if pid == prod.prodId:
                        deleteList.append(prod)
                        ProductServiceImpl.productList.remove(prod)
                        print("Successfully Deleted below Id: ")
                return deleteList
            else:
                print("List is Empty")
        except:
            print("There was an error while removing data.")

    def get_all_product(self):
        try:
            if ProductServiceImpl.productList:
                return ProductServiceImpl.productList
            else:
                return ProductServiceImpl.productList
        except:
            print("There was an error while displaying all products")

    def min_product_price(self):
        try:
            if ProductServiceImpl.productList:
                priceList = []
                for price in ProductServiceImpl.productList:
                    priceList.append(price.prodPrice)
                print('Minimum Product Price Value:', min(priceList))
        except:
            print("There was an error while calculating min product price")

    def max_product_price(self):
        try:
            if ProductServiceImpl.productList:
                priceList = []
                for price in ProductServiceImpl.productList:
                    priceList.append(price.prodPrice)
                print('Maximum Product Price Value:', max(priceList))
        except:
            print("There was an error while calucalating max price")

    def search_by_category(self, cate: str):
        try:
            if ProductServiceImpl.productList:
                prodcatList = []
                for cat in ProductServiceImpl.productList:
                    if cat.prodCategory == cate:
                        prodcatList.append(cat)
                return prodcatList
        except:
            print("There was an error while searching category..")

    def search_by_id(self, pid: int):  # If Product[Present] or  --> None[Absent]
        try:
            if ProductServiceImpl.productList:
                for prod in ProductServiceImpl.productList:
                    if prod.prodId == pid:
                        return prod
        except:
            print("There was error..! While searching id in list.")

    def search_by_vendor(self, ven: str):
        try:
            if ProductServiceImpl.productList:
                vendorList = []
                for prod in ProductServiceImpl.productList:
                    if prod.prodVendor.vendorName == ven:
                        vendorList.append(prod)
                return vendorList
        except:
            print("There was an error while searching vendor..")

    def total_product_price(self):
        try:
            if ProductServiceImpl.productList:
                totalPrice = 0.0
                for prod in ProductServiceImpl.productList:
                    totalPrice = totalPrice + (prod.prodPrice * prod.prodQty)
                return totalPrice
        except:
            print("There was an error while calculating total price..")

    def update_product(self, pid: int):
        try:
            if ProductServiceImpl.productList:
                prodToModify = pid
                productList = ProductServiceImpl.productList
                # search for the record to update
                for prod in productList:

                    if prodToModify == prod.prodId:
                        break
                    else:
                        print("Record not found to modify.. please enter valid product id")
                        # returning false if prod id is not available then control go to main menu.
                        return False
                try:
                    option = int(input(
                        '1. To modify name, 2. To modify price, '
                        '3. To modify vendor, ''4. To modify category '
                        '5. To modify vendor name ''6. To modify vendor adress: '))
                    if option == str:
                        raise
                except ValueError:
                    print("Please Enter Integer Value only..")
                except:
                    print("Unaccepted response.. Please int value only")
                else:
                    if option == 1:
                        try:
                            prod.prodName = input("Enter to modify product name :")
                            if prod.prodName == prod.prodName.isdigit():
                                raise "Its required only string"
                        except TypeError:
                            print("Invalid product name")
                        except:
                            print("Its not valid product name..")
                        else:
                            productList.insert(prod.prodId, prod.prodName)
                            print(prod)
                            print("Updated Product Name Successfully.")
                    elif option == 2:
                        prod.prodPrice = float(input(("Enter to modify Product price:")))
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
        except:
            print("There was an error while updating data..")
