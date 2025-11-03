# Method Overriding :- When Parent and child both have same method 
# Then it excute child class method this is called 

##########################################
#  Method Overriding 
###########################################

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
    
s = SmartPhone(123,"MI",13) 
s.buy()  # Buying a Smartphone  it excute child class method 
