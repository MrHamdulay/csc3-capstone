"""program to do vector calculations in 3 dimensions
yasha longstaff
24 april 2014"""

import math

vector_a = input('Enter vector A:\n')
vector_b = input('Enter vector B:\n')

list1 = vector_a.split()
list2 = vector_b.split() 

def add():
    add = []
    for i in range(3):
        a = eval(list1[i])+eval(list2[i])
        add.append(a)
    print('A+B =', add)

def multiply():
    mult = 0
    for j in range (3):
        m = eval(list1[j]) * eval(list2[j])
        mult += m
    print('A.B =', mult)

def A():
    sqr_A = 0
    for k in range(3):
        A = eval(list1[k])**2
        sqr_A += A
    sqr_A = math.sqrt(sqr_A)
    print('|A| =',"{0:.2f}".format(sqr_A))
        

def B():
    sqr_B = 0
    for p in range(3):
        B = eval(list2[p])**2
        sqr_B += B
    sqr_B = math.sqrt(sqr_B)
    print('|B| =', "{0:.2f}".format(sqr_B))
        

def main():
    add()
    multiply()
    A()
    B()
    
main()