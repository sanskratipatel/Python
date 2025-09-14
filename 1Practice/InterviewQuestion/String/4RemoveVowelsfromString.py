str1 = 'Hello this is me' 
str2 =""
for i in range(0, len(str1)): 
    if str1[i].lower() not in 'aeiou':
       str2 =str2 + str1[i]

print(str2)