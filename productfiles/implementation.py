from products import Product


class ProductImplementation:
    prodList = []

    def add_product(self, details):
        try:
            #ProductImplementation.prodList.append(details) #using list adding details
            #return ProductImplementation.prodList
            """Adding details using files"""
            prodstr = str(details.prodId) + "\t\t" + details.prodName + "\t\t" + str(details.prodPrice) + "\t\t" + str(
                details.prodQty) + "\t\t" + details.prodVendor + "\n"
            with open ('prodlist.txt','a') as f:
                f.writelines(prodstr)
            print("Data added successfully in list")

        except:
            print("There was an error while adding data to the list")

    def add_data_into_file(self):
        try:
            """List data adding into the file"""
            prodLines = []
            if ProductImplementation.prodList:
                for prod in ProductImplementation.prodList:
                    prodstr = str(prod.prodId) + "\t\t" + prod.prodName + "\t\t" + str(prod.prodPrice) + "\t\t" + str(
                        prod.prodQty) + "\t\t" + prod.prodVendor + "\n"
                    prodLines.append(prodstr)

                with open('prodlist.txt', 'w') as f:
                    for line in prodLines:
                        f.writelines(line)
                print("Products are written into the text files..")

        except:
            print("There was an error while writing data to the file")

    def read_data_into_file(self):
        try:
            """Read operation for text file"""
            with open('prodlist.txt','r') as f:
                alllines=f.readlines()
                alllines=[line.strip() for line in alllines]
                prodlines=[]
                for line in alllines:
                    words=line.split("\t\t")
                    prodlines.append(Product(pid=words[0],pnm=words[1],pric=words[2],pqty=words[3],pven=words[4]))
                print(prodlines)
        except:
            print("There was an error while reading data..")
