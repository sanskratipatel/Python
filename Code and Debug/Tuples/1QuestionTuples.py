my_tuple = (1,2,3,4334,54,56,7,7) 
print(my_tuple) 
print(my_tuple[0]) 

s = my_tuple.count(7) 
print(s) 

x =my_tuple.index(2)  
print(x) 

my_list = list(my_tuple) 
my_list.append(100)  
print(my_list)
my_tuple = tuple(my_list) 
print(my_tuple)