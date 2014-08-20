"""Program doing basic vector calculations in 3d
Khanyisile Morudu
20 April 2014"""

import math

#getting inputs
a = input("Enter vector A:\n")
b = input("Enter vector B:\n")


#creating lists from those inputs
a = a.split(" ")
b  =b.split(" ")
add = []
multiply = []

#function that adds all
def add_all(a,b):
    for i in range(len(a)):
        num = (int(a[i]) + int(b[i]))
        add.insert(i,num)
    print("A+B =", add)

#dot rule function
def dot_rule(a,b):
    multi = 0    
    for i in range(len(a)):
        num = (int(a[i]) * int(b[i]))
        multi = multi + num 
    print("A.B =", multi)
    
# function for norm of A
def Norm_allA(num):
    sum  = 0
    for i in range(len(num)):
        sum = sum + (int(num[i]) **2)
    a = "{0:0.2f}"
    final = math.sqrt(sum)
    print("|A| = " + str(a.format(final,2)))
        
#function for norm of B
def Norm_allB(num):
    sum  = 0
    for i in range(len(num)):
        sum = sum + (int(num[i]) **2)    
    a = "{0:0.2f}"
    final = math.sqrt(sum)
    print("|B| = " + str(a.format(final)))
    
    
add_all(a,b)
dot_rule(a,b)
Norm_allA(a)
Norm_allB(b)

    

