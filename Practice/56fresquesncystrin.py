mystr = "hello world" 
result = {} 

for i in range(0 ,len(mystr)):
    if mystr[i] in result:
        result[mystr[i]] +=1 
    else: 
         result[mystr[i]]= 1
print(result)