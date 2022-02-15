class Contact:
    def __init__(self, street=None, city=None, state=None, country=None, pincode=None):
        self.contStreet = street
        self.contCity = city
        self.contState = state
        self.contCountry = country
        self.conPincode = pincode

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''
