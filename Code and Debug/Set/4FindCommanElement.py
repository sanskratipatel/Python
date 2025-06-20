a = [1,2,3,4,5] 
b=[1,2,6,7,9,5] 
my_set1 = set(a) 
my_set2 = set(b) 

my_set3 =(my_set1.intersection(my_set2)) 

list1 = list(my_set3) 
print("LIst of common = ", list1)