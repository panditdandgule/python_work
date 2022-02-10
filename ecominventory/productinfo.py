class Product:

    def __init__(self, pid, pnm, pric, pqty, pven, pcat):
        self.prodId = pid
        self.prodName = pnm
        self.prodPrice = pric
        self.prodQty = pqty
        self.prodVendor = pven
        self.prodCategory = pcat

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n {self.__dict__}\n'''
