#question2 
#used google a lot - still struggling with loops :(

height=eval(input("Enter the height of the triangle:\n"))

def triangle(n):
    for height in range(n):
        print( ' ' * (n-height-1)+ '*' * (2*height+1))
        
triangle(height)        