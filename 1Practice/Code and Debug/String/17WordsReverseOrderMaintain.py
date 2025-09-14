my_str = "hello world" 
str2 = my_str.split()  
str3 = []
for i in range(0,len(str2)): 
   a = str2[i][::-1]   
   str3.append(a) 

r = " ".join(str3)
print(r)
