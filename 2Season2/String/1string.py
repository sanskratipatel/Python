str1 = " Hello World " 
str1 = str1.strip()  
print(str1)
str2 = ""
list1 =str1.split(" ") 

for i in range(len(list1)-1,-1,-1): 
        str2 = str2 + " " + list1[i] 
print((str2).strip())