num = int(input("Enter a number ="))
revnum = num 
rev = 0
while(num >0):
    rev = (rev*10) + (num%10) 
    num = num//10 
print("Reverse of number is",rev) 
if revnum == rev:
    print("Number is palindrome")
else:   
    print("Number is not palindrome")