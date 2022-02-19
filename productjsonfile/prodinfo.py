class Product:
    def __init__(self,pid,pnm,price,pqty,pven):
        self.prodId=pid
        self.prodName=pnm
        self.prodPrice=price
        self.prodQty=pqty
        self.prodVendor=pven


    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n{self.__dict__}\n'''


