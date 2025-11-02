class Person: 
    def __init__(self, name,gender ):
        self.name = name 
        self.gender = gender  


def greet(person) : 
    print(f"My name is {person.name} and my gender is {person.gender} ")  
    p1 = Person("Ved" , "Male")
    return p1

p = Person("Sanskrati" ,"Female") 

f = greet(p) 

print(f.name) 
print(f.gender) 

# >>>>>>>>>>>>>>> Function can take object as input and also return a object also >>>>>>>>>>>>>>>>>>  
# We send a object to function then we send their reference  



# Now we are change object variable value inside a function  and It will change because we send actual Refernce not copy of object
def greet2(person): 
    person.name = "Abhi" 
    print( person.name )  

p2 =Person("Radha" , "Female") 

greet2(p2) 
print(p2.name)