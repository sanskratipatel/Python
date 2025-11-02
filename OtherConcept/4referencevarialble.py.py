class Person: 
    def __init__(self,name_input:str,country_input :str) : 
        self.name = name_input
        self.country= country_input.upper()
    

    def greet(self) : 
        if self.country == 'INDIA' : 
            print(f"Namste {self.name}") 
        else: 
            print(f"Hello {self.name}") 

p = Person('Abhi', 'india') 
print(p.name) 
print(p.country) 
p.greet()
p.gender = "Female"    
# You can create Attribute from outside of that class 
print(p.gender)  

# REFERENCE Variable 

class Person2:
    def __init__(self,name):
        self.n = name 
Person2('b')   # It going to work this is object 
# when we do  ********* P= Person2() ******  then **** P ******** is ReferenceVariable here who just hold the reference of actual object 
p1 =  Person2('q') 
q = p1 
# Now both q and p1 is same now we can create one object and give their referece to n number of vaiables (refernce)
print(p1.n) 
print(q.n)  
# This is same  
p1.n = "wqwd"
print( q.n)  
# Now both have changed  with this p1.n = "wqwd"

