class Product:
    def __init__(self,pid,pnm,pric,pqty,pven):
        self.prodId=pid
        self.prodName=pnm
        self.prodPrice=pric
        self.prodQty=pqty
        self.prodVendor=pven

    def __str__(self):
        return f"""\n{self.__dict__}\n"""

    def __repr__(self):
        return str(self)

#p=Product(1,'Pandit',30000,30,'Flipkart')
#print(p)