str1 = "Hello Guys" 
str1 =str1.strip() 
str1 = str1.replace(" ","")
str1 = str1.lower()
count = 0 
i = 0
while(i < len(str1)): 
    if str1[i] not in 'aeiou': 
        count = count+1
    i = i+1
print(count)