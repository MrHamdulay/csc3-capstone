import math

#ask the user for a function
b=input("Enter a function f(x):\n")
#draw a function within limits (-10,10)
def f():
    for y in range(10,-11,-1):
        for x in range (-10,11):
            g=eval(b.replace("x","("+str(x)+")"))
            if y==round(g):
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
    f ()
if __name__ == "__main__":
    main ()
    
    
    
              