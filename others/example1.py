class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=price

    def full_name(self):
        return f"{self.brand,self.model_name}"

    def make_a_call(self,number):
        return f"calling..{number}"

class SmartPhone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera


smartphone=SmartPhone('Samsung',5,30000,64,128,13)
print(help(smartphone))
