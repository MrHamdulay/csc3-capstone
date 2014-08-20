"""
Plot the function
Yamkela Venfolo
10 April 2014
"""
import math
def functionValue(x,function):#calculates function value
    function=function.replace('x',"("+str(x)+")")#substitutes the x value
    #print(x,function)
    fvalue=eval(function)#calculates the function value
    return round(fvalue)

#Method to plot the function(f(x))
def main():
    function=input("Enter a function f(x):\n")
    xvalues=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
    for fpos in range(10,-11,-1):
        #print(fpos)
        for i in xvalues:
            #print(i)
            fvalue=functionValue(i,function)
            #print(fvalue)
            #Ploting the points
            if fvalue==fpos:
                print("o",end="")
            elif fpos==0 and i==0:
                print("+",end="")
            #X-axis    
            elif fpos==0:
                print("-",end="")
            #Y-axis    
            elif i==0:
                print("|",end="")
            else:
                print(" ",end="")
        print("\n", end="")
if __name__ == "__main__":
    main()
        