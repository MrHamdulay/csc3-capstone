#draw a text-based graph of f(x)
#lebogang masila
#16 april 2014

import math


f=input("Enter a function f(x):\n")

#draw graph of f(x) between (-10,10)
def graph():
    for y in range(10,-11,-1):
        for x in range (-10,11):
            s=eval(f.replace("x","("+str(x)+")"))
            if y==round(s):
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
    
    
    
              