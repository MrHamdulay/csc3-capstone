import math

def main():
    function=input("Enter a function f(x):\n")
    for y in range(10,-11,-1):
        for x in range(-10,11):
            w=round(eval(function))
            if w== y:
                print("o",end="")
            elif x==0 and y==0:
                print("+",end="")                
                
            elif x==0:
                print("|",end="")
            elif y==0:
                print("-",end="")
            else:
                print(" ",end="")
        print()        
main()                
            
                
            
            
    