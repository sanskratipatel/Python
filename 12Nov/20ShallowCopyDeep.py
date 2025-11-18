# shallowCopy :-
# With Equal it create copy with same reference 
# It does not have any problem with Immutable Datatype 
# It have problem with mutable  
my_list = [1,2,3,5] 
li = my_list 
print("Before Update") 
print(li) 
print(my_list) 
print("After Update") 
li[0] = 100 
print(li) 
print(my_list)
# It update both 

# Deep Copy :- It create new Indenpent Copy 

my_list1 = [1,2,3,4,6,7] 
li2 = my_list.copy() 
print(li2) 
print(my_list1) 

li2[0] = 1000 
print(li2) 
print(my_list1) 