# addition, dot product and normalization
# Devaksha Pillay
# 21 April 2014

import math

#Convert input to a list
a = input("Enter vector A:\n")
a = a.split(" ")
b = input("Enter vector B:\n")
b = b.split(" ")

#add lists together
add_lists = [(eval(a[0])+eval(b[0])),(eval(a[1])+eval(b[1])),(eval(a[2])+eval(b[2]))]
print("A+B =",add_lists)

#multiply lists together
multiply_lists = (eval(a[0])*eval(b[0]))+(eval(a[1])*eval(b[1]))+(eval(a[2])*eval(b[2]))
print("A.B =",multiply_lists)

#work out norm of a
num = ((eval(a[0]))**2) + ((eval(a[1]))**2) + ((eval(a[2]))**2)
norm_a = "{:.2f}".format(math.sqrt(num))
print("|A| =",norm_a)

#work out norm of b
num = ((eval(b[0]))**2) + ((eval(b[1]))**2) + ((eval(b[2]))**2)
norm_b = "{:.2f}".format(math.sqrt(num))
print("|B| =",norm_b)