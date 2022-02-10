class Vendor:
    def __init__(self, vid, vnm, vadr):
        self.vendorId = vid
        self.vendorName = vnm
        self.vendorAdr = vadr

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n{self.__dict__}\n'''
