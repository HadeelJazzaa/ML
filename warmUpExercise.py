# Method 1
import numpy as PyIdd
a=PyIdd.identity(5)
print(a)

print("I dentity Matrix using NumPy package")

print("---------------------")
# Method 2
for x in range(0, 5):
    for y in range(0, 5):
        # Here end is used to stay in same line
        if (x == y):
            print("1 ", end=" ")
        else:
           print("0 ", end=" ")
    print()
print("I dentity Matrix without NumPy package")    
 
