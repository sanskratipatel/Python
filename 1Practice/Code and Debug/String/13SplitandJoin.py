my_str = "Hello this is me how are you" 
words = my_str.split() 
print(words) 

print(len(words)) 

for i in range(0 , len(words)-1): 
     print(words[i]) 
print()   
for i in range(len(words)-1,-1,-1): 
     print(words[i]) 

