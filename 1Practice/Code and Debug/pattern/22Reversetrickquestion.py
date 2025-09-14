for i in range(5,0,-1): 
    for j in range(i,0,-1):
       print(j, end=" ")
    print() 

# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1 

for i in range (5 ,0 ,-1):
    for j in range(5,i-1,-1):
        print( i+j-1,end=" ") 
    print() 

# 9
# 8 7
# 7 6 5
# 6 5 4 3
# 5 4 3 2 1  
# num = 1
# for i in range (5 ,0 ,-1):
#     for j in range(5,i-1,-1):
#         print( num,end=" ")  
#         num = num+1
#     print() 
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15 



for i in range (1,6 ):
    for j in range(i,0,-1):
        print( j-1 ,end=" ")  
        # num = num+1
    print()  

# 0
# 1 0
# 2 1 0
# 3 2 1 0
# 4 3 2 1 0