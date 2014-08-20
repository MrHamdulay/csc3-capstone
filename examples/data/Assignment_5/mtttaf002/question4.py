"""program that draws graphs of mathematical functions
tafara mtutu
16 april 2014"""
import math
def newFunction(x):
    #convert cfunction from string and calculate f(x)
    if func.find("math") != -1:
        x_real = x/20 * math.pi*2
    r = eval(func)
    return r

func = input("Enter a function f(x):\n")
#inc = 1/20
for y in range(-10, 11):
    for x in range (0, 21):
        yVal = newFunction(x-10)
        if -y == yVal:
            print("o", sep = "", end = "")
        elif -y-0.5<yVal<-y+0.5:
            print("o", sep = "", end = "")
        elif x == 10 and y == 0:
            print("+", end = "")        
        elif x == 10:
            print("|", end = "") 
        elif y == 0:
            print("-", sep = "", end = "")
        else: print(" ", end = "")
    print()
    