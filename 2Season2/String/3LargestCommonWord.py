str1 =["hlower" , "flow" , "flight"]  
base = str1[0] 
result = ""
if len(str1) ==0: 
    result = ""
else:
    for i in range(0 , len(str1)) : 
        for word in str1[1:]: 
            if i == len(word) or word[i] != base[i]:  
                break
        
        result= result +base[i]

print (result)