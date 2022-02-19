import sys
from ecominventory.services import ProductServices
from ecominventory.productinfo import Product
from myerror import MyError
from collections import defaultdict


class ValueDivision(Exception):
    def __init__(self, arg):
        self.msg = arg

    def __str__(self):
        return repr(self.msg)


class ProductServiceImpl(ProductServices, ValueDivision):
    productList = []  # class level var --> ProductServiceImpl.productList
    allproduct = {}
    productsVendor = {'Flipkart': [], 'Amazon': []}

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
        except MyError as err:
            print(err.msg)
        except:
            print("There was error product was not added.")

    def avg_product_price(self):
        if ProductServiceImpl.productList:
            try:
                totalProductPrice = self.total_product_price()
                avgPrice = totalProductPrice / len(ProductServiceImpl.productList)
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
            print("There was an error while calculating max price")

    def search_by_category(self, cate: str):
        try:
            if ProductServiceImpl.productList:
                prodcatlist = []
                for cat in ProductServiceImpl.productList:
                    if cat.prodCategory == cate:
                        prodcatlist.append(cat)
                return prodcatlist
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
                        '5. To modify vendor name ''6. To modify vendor address: '))
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
                        prod.prodPrice = float(input("Enter to modify Product price:"))
                        productList.insert(prod.prodId, prod.prodPrice)
                        print(prod)
                        print("Updated Product Price Successfully")
                    elif option == 3:
                        prod.prodVendor = input("Enter to modify product vendor:")
                        productList.insert(prod.prodId, prod.prodVendor)
                        print(prod)
                        print("Updated Vendor name successfully..")
                    elif option == 4:
                        prod.prodCategory = input("Enter to modify product category")
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

    def product_names(self):
        try:
            productNames = []
            if ProductServiceImpl.productList:
                for prodnames in ProductServiceImpl.productList:
                    productNames.append(prodnames.prodName)
                return productNames
        except:
            print("There was an error while searching product names")

    def product_quantity(self, pname):
        try:
            quantity = {}
            totalQty = 0
            if ProductServiceImpl.productList:
                for qty in ProductServiceImpl.productList:

                    if qty.prodName == pname:
                        totalQty += qty.prodQty
                        quantity[pname] = totalQty
                    else:
                        print("Product is not available..")
            return quantity

        except:
            print("There was an error while displaying quantity..")

    def display_all_product_quantity(self):
        try:

            if ProductServiceImpl.productList:
                for product in ProductServiceImpl.productList:
                    ProductServiceImpl.allproduct[product.prodName] = ProductServiceImpl.allproduct.get(
                        product.prodName, 0) + product.prodQty
                for product, prodval in ProductServiceImpl.allproduct.items():
                    print(str(product).title(), "Available Quantity is:", prodval)
                return ProductServiceImpl.allproduct

        except:
            print("There was an error while displaying all products..")

    def withdraw_product_quantity(self, pname):
        try:

            if ProductServiceImpl.productList:
                withdrawproduct = int(input("Please Enter How many products you want to buy? "))
                totalproduct = self.product_quantity(pname)
                print(str(pname).title(), "Available Quantity: ", totalproduct)
                try:
                    if len(totalproduct.values()) < 0:
                        raise MyError("Product is not available for selling..")
                except MyError as err:
                    print(err.msg)
                else:
                    for key, value in totalproduct.items():
                        if key == pname:
                            ProductServiceImpl.allproduct[key] = ProductServiceImpl.allproduct.get(key,
                                                                                                   0) - withdrawproduct
                    print(str(pname).title(), "Available quantity After Selling: ", ProductServiceImpl.allproduct)
        except:
            print("There was an error while withdrawing product..")

    def all_product_category_list(self):
        try:
            categoryNames = []
            if ProductServiceImpl.productList:
                for cat in ProductServiceImpl.productList:
                    if cat.prodCategory:
                        categoryNames.append(cat.prodCategory)
                return categoryNames

        except:
            print("While listing all product category.. There was an error..")

    def all_vendors_list(self):
        try:
            vendorsList = []
            if ProductServiceImpl.productList:
                for vendr in ProductServiceImpl.productList:
                    if vendr.prodVendor.vendorName:
                        vendorsList.append(vendr.prodVendor.vendorName)
            return vendorsList

        except:
            print("There was an error while searching vendor list")

    def all_products_by_vendor(self, vname):
        try:
            if ProductServiceImpl.productList:
                for prod in ProductServiceImpl.productList:
                    if prod.prodVendor.vendorName == vname:
                        if prod.prodVendor.vendorName in ProductServiceImpl.productsVendor:
                            ProductServiceImpl.productsVendor[prod.prodVendor.vendorName].append(prod.prodName)

                    # ProductServiceImpl.productsVendor[prod.prodVendor.vendorName]=ProductServiceImpl.productsVendor.setdefault(prod.prodVendor.vendorName,[].append(prod.prodName))
                    # ProductServiceImpl.productsVendor[prod.prodVendor.vendorName].append(prod.prodName)

                return ProductServiceImpl.productsVendor
        except:
            print("There was an error while fetching details..")

    def display_vendor_address(self, vname):
        try:
            vendorAddress = {'Flipkart': [], 'Amazon': []}
            if ProductServiceImpl.productList:
                for prod in ProductServiceImpl.productList:
                    if prod.prodVendor.vendorName == vname:
                        if prod.prodVendor.vendorName in vendorAddress:
                            vendorAddress[prod.prodVendor.vendorName].append(prod.vendorAddr)
                return vendorAddress


        except:
            print("There was an error while displaying address..")
