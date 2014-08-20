# Luke Joseph
# Question 2 of assignment 6
# 2014-04-20
import math
def vector():
    a = input("Enter vector A:\n")
    x = a.split(" ")
    b = input("Enter vector B:\n")
    y = b.split(" ")   # aquiring inputs
    add=[eval(x[0])+eval(y[0]),eval(x[1])+eval(y[1]),eval(x[2])+eval(y[2])]
    print("A+B =",add)
    mult=str((eval(x[0])*eval(y[0]))+(eval(x[1])*eval(y[1]))+(eval(x[2])*eval(y[2])))
    print("A.B =",mult) # Add functions off inputs
    absa = str(round(math.sqrt(((eval(x[0]))**2)+((eval(x[1]))**2)+((eval(x[2]))**2)),2))
    if absa=="0.0":# If statement to eliminate error when input equals zero
        print("|A| = 0.00")
    else:
        print("|A| =",absa)
    absb = str(round(math.sqrt(((eval(y[0]))**2)+((eval(y[1]))**2)+((eval(y[2]))**2)),2))
    if absb=="0.0":
        print("|B| = 0.00")
    else:
        print("|B| =",absb)
    #absolute values of inputs 
vector()