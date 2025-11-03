# Super() Keyword :-  This Keyword to access parent class method from child class 
# When parent and child both have same method  



class Phone : 
    def __init__(self, price,brand, camera):
        print("Inside Parent Constuctor") 
        self.price = price 
        self.brand = brand 
        self.camera = camera 

    def buy(self): 
        print("Buying a Phone") 
  
class SmartPhone(Phone):
    def buy(self): 
        print("Buying a Smartphone")  
        super().buy()
    
s = SmartPhone(123,"MI",13) 
# Inside Parent Constuctor
# Buying a Smartphone
# Buying a Phone
s.buy() 




# Super is always use inside child class 
# Super cannot accept variable 
# Parent does not have access child class 


class Phone : 
    def __init__(self, price,brand, camera):
        print("Inside Parent Constuctor") 
        self.price = price 
        self.brand = brand 
        self.camera = camera 

    def buy(self): 
        print("Buying a Phone") 

class SmartPhone(Phone):
    def __init__(self,price,brand, camera, os,ram):  
        print("Inside smartphone ")
        super().__init__(price,brand,camera )
        self.os = os 
        self.ram = ram 
        print("Inside SmartPhone Constructor")

s = SmartPhone(12334,"Apple" , 13,"Android",2) 
