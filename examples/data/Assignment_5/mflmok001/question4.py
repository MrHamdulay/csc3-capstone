'''graph drawing program
Mokoena Mafologele
16/04/2014'''

import math
#calculates function value
def Function_Value(x,Function):
    #subs x value
    Function=Function.replace('x',"("+str(x)+")")
    F_Value=eval(Function)#calculates the Function value
    return round(F_Value)
# plots the function
def main():
    Function=input("Enter a function f(x):\n")
    
    x_axis=[-10,-9,-8,-7,-6,-5,-4,-3,
            -2,-1,0,1,2,3,4,5,6,7,8,9,10]
    
    #now we have to plot the function
    for Function_position in range(10,-11,-1):
        for i in x_axis:
            
            F_Value=Function_Value(i,Function)
            
            if F_Value==Function_position:
                #each point needs plotting
                print("o",end="")
                
            elif Function_position==0 and i==0:
                #origin plotting
                print("+",end="")
                
            elif Function_position==0:
                #x_axis plotting
                print("-",end="")
                
            elif i==0:
                #y_axis plotting
                print("|",end="")
                
            else:
                
                print(" ",end="")
        print("\n", end="")
        
if __name__ == "__main__":
    main()
                
