# A program to draw an isoceles triangle of a given height using the ‘*’ character. 
# Author: Afika Nyati
# Date: 21 March 2014

def main():
    
    height = eval(input("Enter the height of the triangle:\n"))
    
    gap = (height*2-1)//2
    
    for i in range(height):
        
        print(" "*gap, end ="")
        print("*"*(2*(i)+1))
        gap-=1
        
main()