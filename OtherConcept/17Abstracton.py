# Abstraction :- It means Hiding unnesscary details from user 
# Abstract class :- Is a class that have atleast one abstract method 
# Abstract MethoD -A method that is declared but not implemented (no body).
# We use  @abstractmethod KEYWORKD for that 

from abc import ABC, abstractmethod



class B(ABC): 
    def database(self): 
        print("") 
    @abstractmethod
    def security(self) : 
        pass 

class C(B) : 
    def login(self) : 
        print("Login in App ") 
    
    def security(self):
        print("Security")
        super().security()
M = C()  
M.security() 
M.login() 