#A program to plot a given Function
#Mila Tshaka
#Assingment5
#16th April 

import math
#calculates the value of the Function
def Function_Value(x,Function):
    #substitutes the x value
    Function=Function.replace('x',"("+str(x)+")")
    F_Value=eval(Function)#calculates the Function value
    return round(F_Value)
#This Method will plot the Function
def main():
    Function=input("Enter a function f(x):\n")
    
    x_axis=[-10,-9,-8,-7,-6,-5,-4,-3,
            -2,-1,0,1,2,3,4,5,6,7,8,9,10]
    
    #to plot the function
    for FunctionPosition in range(10,-11,-1):
        for i in x_axis:
            
            F_Value=Function_Value(i,Function)
            
            if F_Value==FunctionPosition:
                #to plot each point
                print("o",end="")
                
            elif FunctionPosition==0 and i==0:
                #to plot the origin
                print("+",end="")
                
            elif FunctionPosition==0:
                #to plot the x-axis
                print("-",end="")
                
            elif i==0:
                #to plot the y axis
                print("|",end="")
                
            else:
                
                print(" ",end="")
        print("\n", end="")
if __name__ == "__main__":
    main()
                