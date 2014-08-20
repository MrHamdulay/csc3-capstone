"""Draw graph of a mathematical function
peter m muriuki"""

import math

#input a function & evaluate the value of the function for values of x
f_str=input("Enter a function f(x):\n")

#draw graph of f(x) within limits (-10,10)
def graph():
    for y in range(10,-11,-1):
        for x in range (-10,11):
            sumx=eval(f_str.replace("x","("+str(x)+")"))
            if y==round(sumx):
                print("o",end="")             
            elif x== 0 and y== 0:
                print("+",end="")
            elif x==0 and y!= 0:
                print("|",end="")
            elif y== 0 and x!=0:
                print("-",end="")
            else:
                print(" ",end="")
        print()
        
def main ():
    graph ()
if __name__ == "__main__":
    main ()
    
    
    
              