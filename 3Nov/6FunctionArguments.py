def print_name(name) : 
    print(name) 

print_name("Abhi") 



def keyword_argument(a,b,c) : 
    print(a,b,c) 

keyword_argument(b=1,a=2,c=3) 

def mix_process_keyword(a,b,c) : 
    print(a,b,c) 

mix_process_keyword(1,b=3,c=4)  

def default_argument(a,b=0,c=4) : 
    print(a,b,c) 
default_argument(1,c =2)  

def variable_length_argument(a,b,*args,**kwargs) : 
    print(a,b)
    print("$$$$$$$$$$$$$$$$$$$")
    for i in args: 
        print(i) 
    for key in kwargs:
        print(key,kwargs[key])
    
variable_length_argument(1,2,3,4, {"a":"abhi",1:4, "name":"me"}) 

def farse_agrument(a,b,*,c,d) : 
    print(a,b,c,d) 

farse_agrument(1,2,c=2,d=4) 

def more_args(*args,c,b) :
    print(c,b) 
    for ar in args :
        print(ar) 

more_args(1,2,3,4,c=4,b=4) 


my_list =[1,2,3,4] 
def unpack(a,b,c,d): 
    print(a,b,c,d) 

unpack(*my_list) 

def unpacke(*args) :
    for i in args:
        print(i) 
unpacke(*my_list) 