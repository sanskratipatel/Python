mystr1= "hello world" 

mystr = list(mystr1)
for i in range(0 , len(mystr)) :
        if i ==0  or i == len(mystr)-1 : 
            if mystr[i].islower():
                 mystr[i] = mystr[i].upper() 
           
        elif mystr[i] == " " : 
            if mystr[i -1].islower() :
                  mystr[i-1] = mystr[i-1].upper() 
            if mystr[i +1].islower() :
                  mystr[i+ 1] = mystr[i+1].upper() 
result = "".join(mystr)
print(result)