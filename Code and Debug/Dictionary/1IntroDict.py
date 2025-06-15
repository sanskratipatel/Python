my_dict = { 
    "name":"abhi", 
    "age": 12,
    "number":43
} 

print(my_dict["name"]) 
print(my_dict["age"]) 
# print(my_dict["Phone"])  throw error 
rs = my_dict.get("name")  
print(rs) 
r = my_dict.get("phone") 
print(r)  # None does not throw error 

K = input("Enter a key = ") 
result = my_dict.get(K) 
if result == None: 
    print("Not exists") 
else : 
    print(result)
    print("Exists")