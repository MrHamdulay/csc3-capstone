#question 2

def isotriangle (h):
    space=h-1 #As in the assignment question
    i=1
    while i<=h:
        print (space*" ","*"*(2*i-1),space*" ",sep="")        
        i+=1 #increases to make it become close to the value of height
        space=space-1 #decrease the space to make it fit the increasing triangle
        
h = eval (input("Enter the height of the triangle:\n"))



isotriangle (h)