# Error or Exception  

# a = 15 
# a =-1
# if a<0: 
#     raise Exception("X should be positive")  

# # we can also use assert 

# assert(a >=0) , "a is not positive" 

try :
    c ="sfs" + "rdd"
    a = 5 / 0 
except ZeroDivisionError as e: 
    print("error" ,e) 
except TypeError as e :
    print("errorrrrrrrrrr",e)
except Exception as e :
    # We got type of exception
    print("An error happend" , e)   
else: 
    print("Every think isfine")

finally : 
    print("Cleaning done")  


class ValueTooHighError(Exception):
    pass

class ValueTooSmall(Exception):
    def __init__(self, message,value):
       self.message = message 
       self.value = value 




def test_value(x):
    if x > 100: 
        raise ValueTooHighError('Value is too high') 
    elif x <3 : 
        raise ValueTooHighError("Value is too small",x)
try: 
    test_value(0) 
except ValueTooHighError as e : 
    print(e) 
except ValueTooSmall as e : 
    print(e.message ,e.value)
   


        

