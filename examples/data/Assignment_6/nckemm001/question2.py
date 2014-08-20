# Emmalene Naicker
# NCKEMM001
# Question 2 

import math

# Get vectors from the user and store it in a list
X = input("Enter vector A:\n").split(" ")

Y = input("Enter vector B:\n").split(" ")

# Convert string elements in arrays to integers 
for i in range (len(X)):
    X[i] = eval(X[i])
    Y[i] = eval(Y[i])
  


add_vectors = []     # Add the vectors
for i in range(len(X)):
    add_vectors.append(X[i] + Y[i]) 
    
    

dot_product = 0
for i in range(len(add_vectors)):\
    dot_product += (X[i] * Y[i])


normal_X = 0
normal_Y = 0


for x in X:
    normal_X += x**2 # Sum of squares
normal_X = math.sqrt(normal_X)# Square root of sum of squares
    
    

for y in Y:
    normal_Y += y**2  # Sum of squares
normal_Y = math.sqrt(normal_Y) # Square root of sum of squares


# Print the output
print("A+B =", add_vectors)
print("A.B =", dot_product)
print("|A| =", "{:.2f}".format(normal_X, 3))
print("|B| =", "{:.2f}".format(normal_Y, 3))



