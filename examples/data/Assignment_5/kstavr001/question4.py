#Assignment 5, Question 4
#Avreyna Kistensamy
#16 April 2014

import math
def main():
    graph = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for i in range(10,-11,-1):
        for p in range(-10,11,1):
            x=p
            g_plot = round(eval(graph))
            #Plot points
            if g_plot == i:
                print("o", end="")
            #Axis meeting
            if i==0 and p==0 and  i != g_plot:
                print("+", end="")
            #Drawing y-axis
            if p == 0 and i != 0 and i != g_plot:
                print("|", end="")
            #Drawing x-axis
            if i==0 and  p!=0 and  i != g_plot:
                print("-", end="")
            else:
                if i != 0:
                    if p != 0:
                        if i != g_plot:
                            print(" ", end="")
        print()
main()