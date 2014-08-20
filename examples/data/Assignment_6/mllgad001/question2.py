# program to do basic vector calculations in 3 dimensions
# mllgad001
# 23 April 2014

import math

vector_a = input("Enter vector A:\n") # prompts user to enter vectors
vector_b = input("Enter vector B:\n")


vectors = vector_a + " " + vector_b
vectors = vectors.split(' ')

def summ(): # define function to calculate vector sum
    x = 0
    y= 3 # set y to 6 (the next number is 6 spaces after the first) 
    list_ = [] 
    for i in range(0, len(vectors)//2, 1):
        integer = (int(vectors[x]) + int(vectors[y])) # add first integer to the third one after it
        list_.append(integer)
        x += 1
        y += 1
    print("A+B =", list_)

def prod(): # define function to calculate the vector product
    x = 0
    y = 3
    a = 0
    for i in range(0, len(vectors)//2, 1):
        prod = int(vectors[x])*int(vectors[y]) # multiply first integer to third one after it
        x +=1
        y +=1
        a += prod # update a each time by adding all product together
    print("A.B =", a) # prints the sum of products
        
def sqr1(): # define function to calculate the square of first vector
    x = 0
    a = 0
    for i in range(3):
        sqr = int(vectors[x])**(2) # square the integer
        x += 1 # add 2 to x ( next number is 2 spaces after last number)
        a += sqr # update a each time by adding all the squares 
    s= math.sqrt(a) # square the total of a
    r = round(s,2)
    print("|A| =", '{0:.2f}'.format(r)) # round off the squared number
    
def sqr2():
    x = 3
    a = 0
    for i in range(3):
        sqr = int(vectors[x])**(2)
        x += 1
        a += sqr
    s= math.sqrt(a)
    r = round(s,2)
    print("|B| =", '{0:.2f}'.format(r))

summ()
prod()
sqr1()
sqr2()