my_str = "hello guys mDe" ; 
my_str2 = my_str.split() 
my_str3 = []
for i in range(0 , len(my_str2)): 
   a = my_str2[i].title() 
   my_str3.append(a)

print(my_str3) 
r = " ".join(my_str3) 
print(r)