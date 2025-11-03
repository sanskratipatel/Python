# NameSpaces : It is a space that hold names or identifiers.
# Namespace is a dict 
# There are 4 types of  name spaces 
# 1. Builtin NameSpaces 
# 2. Global NameSpaces 
# 3. Enclosing Namespaces 
# 4. Local Namespaces 

# LEGB Rule 


# Scope : - Scope is a area where a particular variable
# or namespace is accessable 


# Local and Global  : - if they have same name variable 
# then we have two scopes and two namespaces and it will treat different 
a =3
b =56
def remp():
    b =1
    print(b) 
remp()
print(a) 
print(b) 

# 1
# 3
# 56 
# If python did not find any variable in local then it find in global
a1 = 2 
def temp(): 
    print(a1)

temp() 

# local , global ->editing  
# You cannot edit global variable in local space 
# You can read it but cannot edit it 
# Exception edit using    global keyword
   

def temp(): 
    global a  # with that change should not do 
    a = a+1 
    print(a) 
temp()
print(a)