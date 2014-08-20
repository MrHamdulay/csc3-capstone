'''Plotting the graph of a given function(as input from user)
Inga Ndyoki
17 April 2014'''
import math
def functionValue(x,function):  #calculates the value of entered function at 
    function=function.replace('x',"("+str(x)+")")#substitutes the x value
    #print(x,function)
   
    return round(eval(function)) #calculates the value of function and returns it

#Method to plot the function(f(x))
def main():
    function=input("Enter a function f(x):\n")
    xvalues=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
    #plots the graph
    for fpos in range(10,-11,-1):
        #print(fpos)
        for i in xvalues:
            #print(i)
            fvalue=functionValue(i,function)
            #print(fvalue)
            if fvalue==fpos:
                print("o",end="")#plots the point on the function
            elif fpos==0 and i==0:
                print("+",end="")#plots the origin
            elif fpos==0:
                print("-",end="")#plots the x-axis
            elif i==0:
                print("|",end="")#plots the y axis
            else:
                print(" ",end="")
        print("\n", end="")
if __name__ == "__main__":
    main()
        