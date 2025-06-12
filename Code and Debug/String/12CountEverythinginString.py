my_str = "Abhi1234*&^%" 
alpha = 0 
number = 0 
symbol = 0 
for i in range(0, len(my_str)): 
    if my_str[i].isalpha():
        alpha = alpha+1 
    elif my_str[i].isnumeric():
        number =number+1 
    else: 
        symbol = symbol+1 
print("Alpha = ", alpha) 
print("number= ",number) 
print("Symbol = ",symbol)