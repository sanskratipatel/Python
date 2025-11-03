# What Gets Inherited
# 1.1 Constuctor
# 1.2 Non Private Attributes
# 1.3 Non Private Methods 


# Constructor :- If child dont have constructor It call from 
#                parent class 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class Phone : 
#     def __init__(self, price,brand, camera):
#         print("Inside Parent Constuctor") 
#         self.price = price 
#         self.brand = brand 
#         self.camera = camera 

#     def buy(self): 
#         print("Buying a Phone") 

# class SmartPhone(Phone):
#     pass 

# s = SmartPhone(123,"MI",13) 
# print(s.brand)
# print(s.price) 
# print(s.camera) 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Phone : 
#     def __init__(self, price,brand, camera):
#         print("Inside Parent Constuctor") 
#         self.price = price 
#         self.brand = brand 
#         self.camera = camera 

#     def buy(self): 
#         print("Buying a Phone") 

# class SmartPhone(Phone):
#     def __init__(self, os,ram): 
#         self.os = os 
#         self.ram = ram 
#         print("Inside SmartPhone Constructor")

# s = SmartPhone("Android",2) 
# Inside SmartPhone Constructor  
# If child have its own constructor it excute it 
# So It does not use their variable also   



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Child cannot Access Parent class Private class method and variable 


class Phone : 
    def __init__(self, price,brand, camera):
        print("Inside Parent Constuctor") 
        self.__price = price 
        self.brand = brand 
        self.camera = camera 

    def __buy(self): 
        print("Buying a Phone") 
    
    def get_price(self) : 
        return self.__price
class SmartPhone(Phone):
    def check(self):
        print(self.__price)  
    
s = SmartPhone(123,"MI",13) 
print(s.brand)
print(s.get_price())
print(s.buy())
print(s.check()) 
