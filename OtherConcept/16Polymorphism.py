# PolyMorphism 
# Method Overriding
# Method Overloading 
# Operator Overloading   

# Method Overloading : - Method Overloading means
# having multiple methods with the same name but 
# different parameters in the same class. 

# Python does not support method overloading directly like Java or C++.
# If you define two methods with the same name,
# the latest definition overrides the previous one. 

# For use Indirectly we use function  default argument 

class Shape() : 

    def area(self,raidus) : 
        return 3.14 * raidus *raidus
    
    def area(self , l ,b) : 
        return l * b



# Operator Overloading  :- Operator behaviour changes on the basis 
# input we give like  
#  '+' operator  if we use it with int 
#  5+6 = 11 
# hel + lo = hello
