from collections import Counter 

a = "aaaabbbbbccccccdddd" 
my_counter = Counter(a) 
print(my_counter) 
# Counter({'c': 6, 'b': 5, 'a': 4, 'd': 4}) 

print(my_counter.keys()) 
# dict_keys(['a', 'b', 'c', 'd'])
print(my_counter.values())
# dict_values([4, 5, 6, 4]) 
print(my_counter.most_common(2)) 
# [('c', 6), ('b', 5)] 
print(my_counter.most_common(2)[0][0]) 
# c 
print(list(my_counter.elements())) 
# ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd']
