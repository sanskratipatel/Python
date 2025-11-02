class Person:
    def __init__(self, name ,age): 
        self.name = name 
        self.age = age
    def details(self) : 
        print(f"my name is {self.name} and my age is {self.age} ") 


p = Person("abhi" , 12) 
p.details()
        