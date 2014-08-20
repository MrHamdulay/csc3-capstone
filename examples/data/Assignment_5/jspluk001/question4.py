"""Luke Joseph
JSPLUK001
2014-04-15
question 4 of assignment 5"""
import math
fx=input("Enter a function f(x):\n")
for y in range(10,-11,-1):
    for x in range(-10,11,1):
        fy = round(eval(fx))
        if fy == y and y!=0 and x!=0:
            print("o",end="")        
        elif x==0 and y!=0:
            if fy!=y :
                print("|",end="")
            else: print("o",end="")
        elif y ==0 and x!=0:
            if fy !=y:
                print("-",end="")
            else: print("o",end="")
        elif y==0 and x==0:
            if fy!=y:
                print("+",end="")
            else:
                print("o",end="")
 #       elif fy == y and y!=0 and x!=0:
  #          print("o",end="")
        else:
            print(" ",end="")
    print()
            
        
    