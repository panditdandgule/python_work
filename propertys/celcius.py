class Celcius:
    def __init__(self,temp=0):
        self.__temprature=temp

    @property
    def temp(self):
        return self.__temprature

    @temp.setter
    def temp(self,val):
        if val<-278:
            raise ValueError("It is valueerror")
        print("Temprature")
        self.__temprature=val

cel=Celcius()
cel.temp=-278

