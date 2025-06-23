str1 = "abhi is me" 
spaces = 0
v = 0 
c = 0
for i in range(0,len(str1)):  
    if str1[i].isspace(): 
        spaces = spaces+1 
    elif str1[i].lower() in 'aeiou' : 
        v = v+1 
    elif str1[i].isalpha(): 
        c = c+1
    

print(f"Spaces = {spaces} , consonants = {c} , vowels = {v}")