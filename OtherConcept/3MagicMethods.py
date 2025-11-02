# Dunder Methods  or Magic Methods 
# THOSE ARE special Methods THEY HAVE SUPERPOWER  that ARE LOOK LIKE ___METHOD__ (LIKE __INIT__  constructor) 
# Python have 1500 magic methods 

# In constructor we write this code related to configration like database connection and internet connection 

# we cannot change name of constructor and also python have only onse constructor   

# SELF kEYWORD 
# self is the object of that class we created so that's we use self to call other methods of class from inside class  
# self is currect object (programming have rule that class method can not call each other) 
# We can use any other name in the place of self like abhi, saktimaan   
# Self is always point to current object    


class Fraction : 
    def __init__(self ,x,y) : 
        self.num = x 
        self.deno = y 


         
