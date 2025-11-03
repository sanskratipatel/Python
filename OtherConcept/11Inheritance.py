# “Inheritance: In this concept, a child class inherits methods and variables from its parent class.” 

# Normal Inheritance
class Parent: 
    def __init__(self): 
        self.name = "Abhilasha" 
        self.age= 23 
    def login(self): 
        print('login')  

class Child(Parent): 
    def enroll(self) : 
        print("Enroll into the course") 

a = Parent() 
b = Child() 
print(b.name)   
# In this code if we have child class also a constuctor then when 
# I try b.name then we get error because child class have their own constructor 
# So it does not call parent class construtor  
# If both have constructor then we use super keyword 

