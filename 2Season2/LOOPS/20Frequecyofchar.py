str1  = "HELLOWORLD" 

my_dict = {} 

for i in range(0 , len(str1)) : 
    if str1[i] in my_dict: 
        my_dict[str1[i]] = my_dict[str1[i]] +1 
    else : 
        my_dict[str1[i]] = 1