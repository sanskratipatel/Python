str1 = "MSDFADAM" 
str2 =""
for i in range(len(str1)-1,-1,-1): 
    str2 = str2 + str1[i] 

if str2 ==str1 : 
    print("Yes") 
else :
    print("no")