li = [1,2,9,3,4,5] 
print(li) 
mylist = [2,2.3,"xc",True ] 
print(mylist) 

if 1 in li: 
    print("T") 
else:
    print("f") 

li.sort() 
print(li) 

li1 = [0] *5 
print(li1) 
l2 =[1,2,3] 
l3 = [4,5] 
# l5 = l2 * l3 
# print(l5) 

l1 = [4,5,7,7] 
l2 = l1.copy()    
l2.append(4)
print(l2) 
print(l1) 

listc = [i for i in range(0 , 11)] 
print(listc)

list2 = [i*i for i in range(0 , len(l2))]
print(list2)