# SLLMOG004
#Question 1 of Assignment 3

import math

message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))

space=0
for i in range(len(message)+ 2*thickness,len(message),-2):
    print("|"*space,"+","-"*i,"+","|"*space,sep="")
    space=space+1
for j in range(0,repeat):
    print("|"*thickness,message.center(len(message)),"|"*thickness)
space=thickness -1
for k in range(len(message) + 2,len(message)+(2*thickness) +1, 2):
    print("|"*space,"+","-"*k,"+","|"*space, sep="")
    space-=1