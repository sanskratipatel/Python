mystr = "GREEK"
my_dict = {} 

for i in range(0 , len(mystr)): 
    if mystr[i] in my_dict: 
        my_dict[mystr[i]] =  my_dict[mystr[i]] +1
    else: 
        my_dict[mystr[i]] = 1 
    
print(my_dict) 
char = "" 
count = 0
for key in my_dict : 
   if my_dict[key] > count:
       count = my_dict[key]  
       char = key
print(count , " = ", char)
       
