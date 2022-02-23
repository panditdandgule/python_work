class Celcius:
    def __init__(self,temp=0):
        self.__temprature=temp

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

    def get_temp(self):
        return self.__temprature


    def set_temp(self,val):
        if val<-278:
            raise ValueError("It is valueerror")
        print("Temprature")
        self.__temprature=val

    set_val=property(fget=get_temp,fset=set_temp)

cel=Celcius()
cel.temp=-278
cel.set_val
print(cel)
