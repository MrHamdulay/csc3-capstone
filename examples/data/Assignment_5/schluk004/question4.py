#Graoh function f(x)
#Luke Schwartzkopff
#13 April 2014

import math
graph=""
func = input("Enter a function f(x):\n")

for y in range(10,-11,-1):
    for x in range(-10,11):
        if round(eval(func))==y:
            graph+="o"
        elif x==0 and y==0:
            graph+="+"
        elif x==0:
            graph+="|"
        elif y==0:
            graph+="-"
        else: graph+=(" ")
        
        if x==10:
            graph+=("\n")
            
print(graph)
        
    