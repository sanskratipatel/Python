number = 1251
rev = 0 
number1 = number
while(number1 > 0): 
    rev= (rev *10) + number1 %10  
    number1 = number1 //10 

print(rev)
if rev == number:
    print("Yayyyy") 
else:
    print("No")