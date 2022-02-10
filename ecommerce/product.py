class Product:
    """This is structure of product class holding data and properties"""
    prodCompany = 'PTECH' #product company name

    def __init__(self, pid, pnm, pric,pqty, pven, pcat):
        self.prodId = pid
        self.prodName = pnm
        self.prodPrice = pric
        self.prodQty = pqty
        self.prodVendor = pven
        self.prodCategory = pcat

    def __str__(self):
        return '{}, {}, {}, {},{},{}\n'.format(self.prodId, self.prodName,
                                            self.prodPrice,self.prodQty, self.prodVendor,
                                            self.prodCategory)

    def __repr__(self):
        return str(self)
