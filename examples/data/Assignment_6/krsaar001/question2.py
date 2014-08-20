# Aaron Krishna
# 24 April 2014
# Manipulating vectors

a1, a2, a3 = input("Enter vector A:\n").split(" ") #requests three vector numbers
vectorA = [eval(a1), eval(a2), eval(a3)] #array
b1, b2, b3 = input("Enter vector B:\n").split(" ") #see line 5
vectorB = [eval(b1), eval(b2), eval(b3)] #see line 6

def add_vector(a, b): #function that adds vectors
   new_vector = [] #store the new added values
   for position in range(3):
      new_vector.append(a[position] + b[position]) #adds new value to array
      
   return new_vector

def multiply_vector(a, b): #fuction that multiplies vectors
   multiply = 0 
   for position in range(3):
      multiply = multiply + (a[position] * b[position]) #sums the products of the two existing vectors 
      
   return multiply

def norm_vector(n): #function that calculates the norm of a vector
   import math
   norm = 0
   for position in range(3):
      norm = norm + (n[position]**2) # ** is the same as to the power of
   norm = math.sqrt(norm) #rounds off to two decimal places
   return norm

print("A+B =", add_vector(vectorA, vectorB))
print("A.B =", multiply_vector(vectorA, vectorB))
print("|A| =", "{0:.2f}".format(norm_vector(vectorA)))
print("|B| =", "{0:.2f}".format(norm_vector(vectorB)))