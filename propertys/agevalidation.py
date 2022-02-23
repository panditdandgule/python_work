class Geeks:
    def __init__(self):
        self._age=0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,val):
        try:
            if val<18:
                raise ValueError("Sorry Your age is below criteria")
        except ValueError as e:
            print(e)
        self._age=val

mark=Geeks()
mark.age=17
print(mark.age)