import math
def main():
    function=input("Enter a function f(x):\n")
    
    for y in range(10,-11,-1):
        for x in range(-10,11,1):
            f=eval(function)
            f=round(f)
            if f==y:
                print("o", end="")
            elif x==0 and y==0 and f!=y:
                print("+", end="")            
            elif x==0 and f!=y:
                print("|", end="")
            elif y==0 and f!=y :
                print("-", end="")
            
            else:
                print(" ", end="")
        print()
main()
            
            
            
            
    