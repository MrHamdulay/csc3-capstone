"""Naveet Baitchu
cartesian plane
17/04/14"""



f=input("Enter a function f(x):\n")
for y in range(10,-11,-1):
       for x in range(-10,11):
              if y==eval(f):
                     print("o",end="")   
              elif x==y==0:
                     print("+",end="")
              elif x==0: 
                     print("|",end="")
              elif y==0:
                     print("-",end="")
              else:
                     print(" ",end="")            
       print()
    

    
