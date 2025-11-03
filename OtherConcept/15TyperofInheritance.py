# Types Of Inheritance 
# Single Inheritance 
    # Parent ---> child  

# MultiLevel Inheritance 
    # grandfather ---> parent ---> child 

# Multiple Inheritance 
# Parent1 + Parent2 → Child

# Hierarchical Inheritance 
#        Parent
#       /      \
#   Child1    Child2
          
# Hybrid 

# Example: combination of Multiple + Multilevel
# class A:
#     pass

# class B(A):
#     pass

# class C:
#     pass

# class D(B, C):   # Hybrid Inheritance
#     pass



# | Concept             | Meaning                                                          |
# | ------------------- | ---------------------------------------------------------------- |
# | **Diamond Problem** | Shared parent class called multiple times                        |
# | **Why It Happens**  | Multiple inheritance without order management                    |
# | **Python Solution** | Uses `super()` + **MRO (C3 Linearization)**                      |
# | **Effect**          | Each class constructor runs exactly once, in a predictable order |
# | **Check Order**     | Use `ClassName.mro()` or `help(ClassName)`                       |
