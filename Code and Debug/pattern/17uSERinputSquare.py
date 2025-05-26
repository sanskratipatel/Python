n = int(input("Enter the number ="))  
# Enter the number =8
# 1 1 1 1 1 1 1 1
# 2 2 2 2 2 2 2 2
# 3 3 3 3 3 3 3 3
# 4 4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5
# 6 6 6 6 6 6 6 6
# 7 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8 
for i in range(1, n+1):
    for j in range(1,n+1):
        print(i, end=" ") 
        print(j,end=" ")
    print() 

# Enter the number =6
# 1 1 1 2 1 3 1 4 1 5 1 6
# 2 1 2 2 2 3 2 4 2 5 2 6
# 3 1 3 2 3 3 3 4 3 5 3 6
# 4 1 4 2 4 3 4 4 4 5 4 6
# 5 1 5 2 5 3 5 4 5 5 5 6
# 6 1 6 2 6 3 6 4 6 5 6 6 


for i in range(1, n+1):
    for j in range(1,n+1):
        print(i, end=" ") 
        print(j,end=" ")
    print() 

# Enter the number =5
# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1
for i in range(n ,0,-1): 
    for j in range(n,0,-1):
        print(i,end=" ") 
    print() 


# Enter the number =5
# 5 5 5 4 5 3 5 2 5 1
# 4 5 4 4 4 3 4 2 4 1
# 3 5 3 4 3 3 3 2 3 1
# 2 5 2 4 2 3 2 2 2 1
# 1 5 1 4 1 3 1 2 1 1
for i in range(n,0 ,-1):
    for j in range(n,0,-1):
        print(i,end=" ")
        print(j,end=" ") 
    print()