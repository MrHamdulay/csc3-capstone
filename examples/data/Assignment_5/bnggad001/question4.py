# Gadziraiushe Bangure: BNGGAD001
#Assignment 5: This is a program to draw a text-based graph of a mathematical function f(x)on 20 unit axes
# Written by ~Shay~
# Date: 18/04/2014



import math
f=input("Enter a function f(x):\n")
for y in range(10,-11,-1):
    for x in range(-10,11):
        if round(eval(f))==y:
            if x!=10: print("o",end="")
            else: print("o")
        elif y==0:
            if x==0: print("+",end="")
            elif x==10: print("-")
            else: print("-",end="")
        elif x==0: print("|",end="")
        elif x!=10: print(" ",end="")
        else :
            print(" ")
            break

#finish=input("")