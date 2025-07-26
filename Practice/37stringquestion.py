my_str = "34w4fsvdfgsa" 
result = ""
for i in range(0 , len(my_str)): 
    if my_str[i].islower: 
        result = result + my_str[i].upper()
print(result)