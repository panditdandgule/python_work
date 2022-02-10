class Vendor:
    """This is structure for the vendor holding attributes and methods"""
    def __init__(self, vid, vnm, vadr):
        self.vendorId = vid
        self.vendorName = vnm
        self.vendorAddr = vadr

    def __str__(self):
        return '{},{},{}\n'.format(self.vendorId, self.vendorName, self.vendorAddr)

    def __repr__(self):
        return str(self)
