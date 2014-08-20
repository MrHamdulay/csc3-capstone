#program to plot simple graph of any inputed function of x between -10 and 10
#Created by Jenna Lake
#Date:15/4/2014

import math 

def graph():
    v=input("Enter a function f(x):\n")
    y_inc=1/20
    
    for y in range(-10,11):
        y=-y #need to invert the graph
        for i in range(-10,11,):
            k=i
            newK= "("+str(k)+")"
            w=v.replace("x",newK) #need to replace imputed x with a variable which can be manipulated
            k_real=eval(w) #convert to intergers
            k_real=round(k_real) # rounds values so that all values can match a y value(which are only integers)
            if y==k_real:
                print("o",end="")
            elif k==0 and y==0:
                print("+",end="")                
            elif y==0:
                print("-",end="")
            elif k==0:
                print("|",end="")
            elif y != k_real:
                print(" ",end="")
            
        print()
graph()
