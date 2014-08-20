#question2.py
#A program to draw an isoceles triangle of a given height using the * character
#Author: Michelle Njoroge

def main():
    height=eval(input("Enter the height of the triangle:\n"))
    gap=" "
    for i in range(height):
        print((height-i-1)*gap,"*"*((2*i)+1),sep="")
main()

        
        
        