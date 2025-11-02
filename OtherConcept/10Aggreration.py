# What is Aggreration ? 
# It means Has A Relationship 
# like this --- > customer has a address 
# like ---> School have students 


# Straight Forward Caase Print Address 
# class Customer : 
#     def __init__ (self, name, gender, address):
#         self.name = name 
#         self.gender = gender 
#         self.address = address 
#     def print_address(self) : 
#         print(self.address.city , self.address.pin , self.address.state)
# class Address: 
#     def __init__(self,city,pin,state) : 
#         self.city = city 
#         self.pin = pin 
#         self.state=state 


# add1 = Address("Bhopal", 452010, "M.P.") 
# cus = Customer('Abhilasha','Female', add1 ) 

# cus.print_address() 




# In thisif we make pin private  then it did not print addressand show error 
# If we want to print it then we use getter and setters
class Customer : 
    def __init__ (self, name, gender, address):
        self.name = name 
        self.gender = gender 
        self.address = address 
    def print_address(self) :  
        # Use Getter to get city 
        print(self.address.get_city() , self.address.pin , self.address.state)
class Address: 
    def __init__(self,city,pin,state) : 
        self.__city = city 
        self.pin = pin 
        self.state=state 
    def get_city(self): 
        return self.__city

add1 = Address("Bhopal", 452010, "M.P.") 
cus = Customer('Abhilasha','Female', add1 ) 

cus.print_address()