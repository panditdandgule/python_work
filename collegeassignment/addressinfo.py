class Address:
    """This is structure of address class"""
    def __init__(self, city, state, pincode):
        self.city = city
        self.state = state
        self.pincode = pincode

    def __str__(self):
        return """{} {} {}\n""".format(self.city,self.state,self.pincode)

    def __repr__(self):
        return str(self)
