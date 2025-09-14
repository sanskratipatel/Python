mystr = "Hello World" 
freq = {} 
for i in range(0 ,len(mystr)):
    if mystr[i] in freq : 
          freq[mystr[i]] += 1 
    else: 
         freq[mystr[i]] = 1
     
print(freq)