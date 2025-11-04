from itertools import permutations 

a = [1,2,3] 
perm = permutations(a) 
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(list(perm)) 

