"""Drawing a text-based graph
Yondela Nkwali
14 April 2014"""

import math

function=input("Enter a function f(x):\n")
#make axes
yinc=1/20
#xpos=function.find("x")
#if xpos!=0:
 #       function=(function[:xpos]+"*"+function[xpos:]) (THEY WON'T TEST THIS!!)
#function=replace(function,"^","**")
function=function.replace("^","**")
#if function[:3]=="sin":
#sin=function[:3]
#function=function.replace(sin,"math.sin")
for y in range(10,-11,-1):
        for x in range(-10,11):
                func=round(eval(function))     
                if func==y:
                        print("o",end="")
                elif x==0 and y==0:
                        print ("+",end="")
                elif x == 0:
                        print ("|",end="")
                elif y == 0:
                        print ("-",end="")
                else:
                        print (" ",end="")
                
        print ()            
            
            
#ask for function
