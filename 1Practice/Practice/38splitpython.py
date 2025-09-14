a = "Hello world this is me"
words = a.split() 
print(words) 

for i in range(0 , len(words)):
    for j in range( len(words[i])-1 ,-1,-1 ): 
        print(words[i][j] , end ="")  
    print(end= " ")

print()  
list1 = ["fds" ,"raw","efasda"]  

str1 = " ".join((list1))
print(str1)  

mystr1 = " ".join(str(i)[::-1] for i in list1)
print(mystr1)
