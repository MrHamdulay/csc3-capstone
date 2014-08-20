# question2
# A program to draw a triangle
# Mpho Natalie Raselo

H=eval(input("Enter the height of the triangle:\n")) 

def x(H,W):
    gap=(H//2)-1
    for i in range (0,H,2):
        print(" "*gap,end="")
        print(W*(i+1))
        gap-=1
       
x(H*2,"*")