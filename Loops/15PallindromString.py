num = int(input("Enter the number = ")) 
num2 =num 
rev =0
while(num>0):
    rev = (rev*10) +(num%10) 
    num =num//10 
if(rev == num2):
    print("Number is pallindrom") 
else:
    print("Not")