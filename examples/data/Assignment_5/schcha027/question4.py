# Assignment 5 Question 4
import math
funct = input("Enter a function f(x):\n")

for y in range(-10,11):
    for i in range(-10,11):
        newI="("+str(i)+")"
        newfunct=funct.replace('x',newI)
        evalfucnt=-eval(newfunct)
        newevalfunct=round(evalfucnt)
        if newevalfunct==y:
            print("o",end="",sep="")
        elif y==0 and i==0:
            print("+",end="",sep="")
        elif y==0:
            print("-",end="",sep="")        
        elif i==0:
            print("|",end="",sep="")        
        else:
            print(" ",end="",sep="")
    print("")
    
#for i in range(0,21):
    
    #if 0<i<11:
        #print(" "*10,"|"," "*10,sep="")
    #elif i==11:
        #print("-"*10,"+","-"*10,sep="")
    #elif 11<i<21:
        #print(" "*10,"|"," "*10,sep="")
