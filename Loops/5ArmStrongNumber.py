num = int(input("Enter a number ="))   
armnum = num
sum = 0 
i = 0 
while(num >0) : 
    sum = sum + (num %10) **3 
    # print("Sum of Cube of first",num,"number is",sum)
    num = num //10 
   
if (armnum == sum) :
    print(armnum,"is an Armstrong number")