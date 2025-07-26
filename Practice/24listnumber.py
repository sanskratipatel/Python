
count = 0
count1=0
list1 =[10,3,34,6,56,7,5,43,4,657,5464,32,5,43,8,5] 
for i in range(0 , len(list1)):
    if list1[i] %2 == 0 :
        count = count+1 
    if list1[i]%2 ==0 and list1[i]%5 == 0 : 
        count1 = count1+1
print(count1) 
print(count)
