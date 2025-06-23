str2 = "(a+b)+c+(d))))" 
str1 =""
for i in range (0,len(str2)) : 
    if str2[i] == ')' or str2[i] =='(': 
        continue
    str1 = str1 + str2[i] 

print(str1)