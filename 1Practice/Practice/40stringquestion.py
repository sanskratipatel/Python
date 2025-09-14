mystr = "hello guys this is me" 
result = ""
for i in range(0 , len(mystr)):
    if i == 0 : 
       result= result +  mystr[0].upper() 
    elif mystr[i-1] == " ": 
        result = result+ mystr[i].upper()  
    else: 
        result = result+mystr[i] 
print(result)

