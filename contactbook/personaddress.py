class PersonAddress:
    def __init__(self,city,state,country,pin):
        self.city=city
        self.state=state
        self.country=country
        self.pin=pin

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''


