# Question 2

height=eval(input("Enter the height of the triangle:\n"))

def tri(height):

    space=height-1
    
    for i in range(height):
        print(' '*space, end='')
        print("*"*(2*i+1))
        space=space-1

tri(height)