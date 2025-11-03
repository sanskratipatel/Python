# Decorator :- A Decorator in python is a function that receive 
# another function as input and add some functionality (decoration) 
# to it and return it 

# There is two type of decorators 
# BuiltIn :- @staticmethod , @classmethod, @property, @abstractmethod 
# User Defined Decorator :- That user Create 


def greet(func) : 
    def wrapper():
        print("Hello Good Morning") 
        func() 
        print("Byeeeeee") 
    return wrapper

def hello():
    print("This is Hello") 

g = greet(hello) 
g() 




def addfive(func) :
    def wrapper(num) : 
        ans = func(num)
        ans = ans +5 
        return ans 
    return wrapper

def number(num): 
    return num 

f = addfive(number)
print(f(4))

@addfive
def number2(num):
    return num +1000 

print(number2(1)) 


import time 

def timer(func):
    def wrapper(*args): 
        start = time.time() 
        func(*args) 
        end = time.time() 
        print(f"Time taken {end-start}") 
    return wrapper 

@timer
def hello_guys():
    print("Hello world")
    time.sleep(1) 

hello_guys()

@timer
def dispaly(): 
    print("Somethink !!!!!!!!!11")  
    time.sleep(1)

dispaly() 

@timer
def square(num) :
    time.sleep(2) 
    print(num **2) 

square(2)

@timer
def power(a,b) : 
    time.sleep(1) 
    print(a**b) 

power(4,2) 



# Check Datatype Function  

def check_type(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0]) == data_type : 
                func(*args) 
            else: 
                raise TypeError("Wrong datatype")
        return inner_wrapper
    return outer_wrapper 

@check_type(int)
def square(num): 
    print(num ** 2) 

square(2)  

@check_type(str)
def helloo(s) : 
    print(s) 

helloo("wqew")
