class Address:
    def __init__(self,city,state,country):
        self.city=city
        self.state=state
        self.country=country

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''