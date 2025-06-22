num = [2,34,5,7,7,5,3,4,234,5] 

# for i in range(len(num)-2, -1,-1) :
#     for j in range(0,i+1):
#         if num[j] > num[j+1]:
#             num[j] ,num[j+1] = num[j+1] ,num[j]  
    

# print(num)


for i in range(0,len(num)-1):
    for j in range(1,i): 
        num[j] > num[j-1] 
        num[j], num[j-1] = num[j-1] ,num[j] 

print(num)