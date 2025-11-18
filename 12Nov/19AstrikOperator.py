result = 5 ** 2 
# POWER Operation
print(result)  
list1 =[0] * 10 
# It create list with 10 Zero
print(list1) 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lost2 = [1,2] * 10 
print(lost2) 
# [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2] 

def fool(a,b,*args,**kwargs): 
    print(a ,b) 
    for arg in args:
        print(arg) 
    for key in kwargs:
        print(key , kwargs[key]) 

list1 = [3,4,6,7,3]
my_dict = {"a":2,"f":5}
fool(1,2,2,list1,my_dict) 


my_list = [1,2,3,45] 
# Unpack a list
def f(a,b,c,d):
    print("&&&&&&&&&&&&&&&&&&&&&&")
    print(a,b,c,d) 
f(*my_list) 

def g (*args):
    for a in args:
        print(a) 
g(*my_list)


