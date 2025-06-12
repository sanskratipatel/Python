my_string  = "AdsdASDS" 
lower_count = 0
upper_count = 0
for ch in range(0, len(my_string)-1):
    if my_string[ch].isupper():
        upper_count = upper_count+1 
    elif my_string[ch].islower():
        lower_count = lower_count +1 
print("lower count =",lower_count) 
print("Upper_count =",upper_count)


for i in range(0, len(my_string)-1): 
    ascii = ord(ch) 
    