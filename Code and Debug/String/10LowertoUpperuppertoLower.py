my_str = (input("Enter the String = ")) 
result= "" 


for i in range(0,len(my_str)): 
    if my_str[i].islower():  
        one = my_str[i].upper()
        result = result + one
    elif my_str[i].isupper(): 
        two = my_str[i].lower() 
        result = result + two 
    else : 
        result = result+my_str[i]
print(result)