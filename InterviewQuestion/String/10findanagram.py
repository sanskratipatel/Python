str1 = "abhi" 
str2 = "bhia" 

str1 =sorted(str1.lower()) 
str2 = sorted(str2.lower()) 
print(str1) 
print(str2)
if str1 == str2: 
    print("Anangram ",str1)