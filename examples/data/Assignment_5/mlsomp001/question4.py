#program to create a graph
#omphemeste molusi
#17 april 2014


import math
def functionValue(x,function):
    function=function.replace('x',"("+str(x)+")")
    fvalue=eval(function)
    return round(fvalue)

def main():
    function=input("Enter a function f(x):\n")
    xvalues=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
    
    for fpos in range(10,-11,-1):
        for i in xvalues:
            fvalue=functionValue(i,function)
            if fvalue==fpos:
                print("o",end="")
            elif fpos==0 and i==0:
                print("+",end="")
            elif fpos==0:
                print("-",end="")
            elif i==0:
                print("|",end="")
            else:
                print(" ",end="")
        print("\n", end="")
if __name__ == "__main__":
    main()
        