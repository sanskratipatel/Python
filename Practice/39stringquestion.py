mystr = "python is good" 

mystr2 = mystr.split(" ") 

print(mystr) 
for i in range( len(mystr2)-1 ,-1 ,-1) : 
    print(mystr2[i] ,end=" ") 
print(type(mystr2))
add1 = " ".join(mystr2) 
print(type(add1))