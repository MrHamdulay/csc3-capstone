#Shriya Roy
#16 April 2014
#program to draw sine graph
import math

def main():
    # getting input from user
    a=input("Enter a function f(x):\n")
    #computing the graph
    for y in range(10,-11,-1):
        for x in range(-10,11):
            plot_pt= round(eval(a))
            if plot_pt==y:
                print("o", end='')
                
            elif y==0 and x==0:
                print("+", end='')
                
            elif x==0 :
                print("|", end='')
            elif y==0 :
                print("-", end='')
            
            else:
                print(" ", end='')
        print()
main()
