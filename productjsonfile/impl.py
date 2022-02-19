from prodinfo import Product

import json

class ProductImpl:
    filename='product.json'
    prodList=[]
    def add_data_into_json_file(self,details):
        try:
            prodlistJson=[]
            """Using user inputs created json file"""
            # with open(self.filename,'w') as f:
            #     data=details.prodId,details.prodName,details.prodPrice,details.prodQty,details.prodVendor
            #
            #     json.dump(details,f)
            #     print("Data added successfully in json file..")


            """Using list we are created json file"""
            ProductImpl.prodList.append(details)
            for prod in ProductImpl.prodList:

                prodlistJson.append(prod.__dict__)

            with open(self.filename,'w') as file:
                json.dump(prodlistJson,file)
            print("Data added successfully..")
        except:
            print("There was an error while adding data to the file")

    def display_data_json_file(self):
        with open(self.filename,'r') as file:
            data=json.load(file)

            for item in data:
                print(item)