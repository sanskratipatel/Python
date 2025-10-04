str1 = 'HELLO WORLD' 

str1 = str1.split(' ') 
print(str1) 
str2 = ""
for i in range(0 , len(str1)):  
    for j in range( len(str1[i])-1 ,-1 ,-1) :  
        str2 = str2 + str1[i][j] 
    str2 = str2 + " "
print(str2)

