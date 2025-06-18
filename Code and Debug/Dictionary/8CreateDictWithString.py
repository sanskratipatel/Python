str = input( "Enter a string = ")
my_dict = {} 
for i in range(0,len(str)): 
    if  str[i] in my_dict:
        my_dict[str[i]] += 1 
    else: 
        my_dict[str[i]] =1 
print(my_dict)