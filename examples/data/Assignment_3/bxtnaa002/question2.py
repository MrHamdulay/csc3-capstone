# question2.py
# program to draw an isoceles triangle of a given height using the "*" character
# author: bxtnaa002

h = eval(input("Enter the height of the triangle:\n"))
gap = h-1  
for i in range(1,h*2,2):
        print(" "*gap,end="") 
        print("*"*i)
        gap=gap-1