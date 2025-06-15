my_dict = { 
  "name":"ABHI",
  "age":23, 
  "list":[23,435,32,324]
} 
print(my_dict) 
my_dict["list"] =[34]
my_dict["age"] = 12133 
print(my_dict)    # It will update value  

my_dict["me"] = "hello"   # It will add new value in dict
print(my_dict) 

# Methosd 2 

my_dict.update({"marks":99 , "add" :45 , "name":"sanskrati"}) 
print(my_dict)

