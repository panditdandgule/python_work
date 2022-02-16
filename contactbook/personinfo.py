from personaddress import PersonAddress

class PersonInfo:
    def __init__(self,pid=None,pnm=None,pdob=None,pemail=None,pcont=None,padr=None):
        self.personId=pid
        self.personName=pnm
        self.personDob=pdob
        self.personEmail=pemail
        self.personContact=pcont
        self.personAdr=padr
    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''







#p1=PersonAddress('Pune','Mh','India',413780)
#p=PersonInfo(1,'Pandit',19021991,'pdandgule@dstws.com',9623639868,p1)
#print(p)
