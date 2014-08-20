"""program to do basic vector calculations in 3 dimensions: addition, dot product and normalization
Mick Perring
23 April 2014"""

import math

a = input("Enter vector A:\n") # user input vector A
b = input("Enter vector B:\n") # user input vector B

# splits vectors A and B into their seperate values
a = a.split(" ")
b = b.split(" ")

# converts vector values into integers and assigns each a seperate variable
aa = int(a[0])
ba = int(a[1])
ca = int(a[2])

ab = int(b[0])
bb = int(b[1])
cb = int(b[2])
    
def add():        # add function adds and prints the sum of vectors A and B (in list form)
    x = aa + ab
    y = ba + bb
    z = ca + cb
    
    add = [] # adds values to list
    add.append(x)
    add.append(y)
    add.append(z)
    
    print ("A+B =", add)
    
def mult():       # mult function multiplies and prints the product of vectors A and B
    ans = aa*ab + ba*bb + ca*cb
    print ("A.B =", ans)

# modA and modB functions calculate and print the norm of vector A and vector B 
    
def modA():
    ans = math.sqrt(aa**2 + ba**2 + ca**2) # calculates norm (sqrt of sum of squares)
    a = "|A| = {0:.2f}"
    print(a.format(ans))
    
def modB():
    ans = math.sqrt(ab**2 + bb**2 + cb**2) # calculates norm (sqrt of sum of squares)
    a = "|B| = {0:.2f}"
    print(a.format(ans))
    
def main():     # main function runs the four functions
    add()
    mult()
    modA()
    modB()
    
main()