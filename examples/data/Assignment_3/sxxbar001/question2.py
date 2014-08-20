#Assignment 3
#Question 2
#25 March 2014
#Program to create an isosceles triangle

height=eval(input("Enter the height of the triangle: \n"))

def tri(height):
    gap=height-1
    star=1
    for i in range(height):
        print(" "*gap,end="")
        print('*'*star)
        gap=gap-1
        star=star+2
        
tri(height)