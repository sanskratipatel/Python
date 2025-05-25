num = int(input("Enter a number =")) 
i =2
while(num>i): 
    num = num/i
    if(num >=2): 
        print("not Prime Number")
        break
    else:
        print(" Prime Number")
    i = i+1
