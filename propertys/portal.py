class Portal:
    def __init__(self):
        self._name=''

    #using property decorator
    @property
    #getter method
    def name(self):
        return self._name

    @name.setter
    def name(self,val):
        if val=='':
            print("Invalid name")
        else:
            self._name=val

    @name.deleter
    def name(self):
        del self._name

p=Portal()
p.name=''
p.name='pandit'
print(p.name)
del p.name
#print(p.name)