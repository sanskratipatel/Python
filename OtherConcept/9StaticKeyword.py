# Static Variable (Vs Instance Variable)  
# Static Variable is class variable 
# Instance variable is object variable 
# For every object value of instance variable is different 
# But static variable value is same

# For static variavle use we  >>>>>>>>>>>>  classname.staticvariablename 
# Like pin should instance variable because every one have different pin 
# Bank name for all customer same so it will be instance variable 


class Atm :
    __counter = 1    # This is Static Ketword 
    def __init__(self):
        self.pin = "" 
        self.balance = 0  
        self.c_id = 0 
        self.c_id = self.c_id +1   
        self.c_id1 = Atm.__counter
        Atm.__counter = Atm.__counter + 1 
    # This is static method you did not need to create object 
    # to access them just access them with class name 
    # Like Atm.get_counter 
    @staticmethod 
    def get_counter() : 
        return Atm.__counter 
    
    def set__counter(self, c): 
        Atm.__counter = c  

        # If we define it here c_id then it is instance vaiable 
        # An it reset everytime when we create its object 
        # And for all object is going to =1  
        # NOW we create Static vaiable 

a= Atm()  
# print(a.c_id)
print(a.c_id1)
a1 = Atm() 
# print(a1.c_id) 
print(a1.c_id1) 
a2 = Atm() 
# print(a2.c_id)
print(a2.c_id1) 