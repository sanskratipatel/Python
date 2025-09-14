num = int(input ("Enter the number = "))  
rev = num 
p = 0
while num > 0 :
   p  = (p*10) + num %10  
   num = num // 10 
if (p == rev) : 
   print("Pallindrom")
else: 
   print("Nope")