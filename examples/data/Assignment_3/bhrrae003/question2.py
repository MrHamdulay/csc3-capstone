#Raeesa Behardien
#BHRRAE003
#Assignment 3 - 28 March 2014

#Question 2
#Program to draw an isosceles triangle

ht=eval(input("Enter the height of the triangle:" '\n'))

a=ht-1
b=1
space=" "*a
for i in range(ht):
    print(space,"*"*b, sep="")
    a-=1
    b+=2
    space=" "*a
    

