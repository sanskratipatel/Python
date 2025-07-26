mystr= "FGFGgfffg"

lower_count = 0
upper_count = 0
for i in range(0 , len(mystr)):
    if mystr[i].isupper():
        upper_count = upper_count +1 
    elif mystr[i].islower() : 
        lower_count = lower_count+1  
print(lower_count) 
print(upper_count) 
