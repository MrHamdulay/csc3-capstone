#WHTBAS001
#ASSIGNMENT 3
#QUESTION 2
#25-03-2014

def triangle(n):
    for i in range(n):
        reverse = n-i-1
        nostars = 2*i + 1
        print(" "*reverse, "*"*nostars, sep="", end="\n")

height = int(eval(input("Enter the height of the triangle:\n")))

triangle(height)

#Done