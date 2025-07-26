x = {"name": "abhi" , "marks" : 324 , (12,43,4):43 } 
print(x) 
my_dict = {"name":"abhi" , "marks" :2343 , 32:343} 

print(my_dict["name"]) 
r = my_dict.get("Name")  
print(r)
# k = input("Enter the key === ") 
# result = my_dict.get(k) 

# if result is not None:
#     print(result) 
# else:
#     print("Not exists") 

print(my_dict) 
my_dict["names"] = "sanskrati"   # it add key if not exists 
print(my_dict) 

my_dict.update({"marks" : 223, "age":342}) 
print(my_dict) 

del my_dict["names"] 
print(my_dict) 
my_dict.clear() 
print(my_dict)