str = "Abhi" 
rev = "" 

for i in range(len(str)-1,-1,-1) : 
    rev =  rev + str[i]


if rev == str : 
    print(f"Pallindrom  sre ={str} rev = {rev} ") 
else: 
    print(f"Not pallindrom {str} and rev {rev}")