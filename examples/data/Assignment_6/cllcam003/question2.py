#Program that completes mathematical calcuations with lists
#Cameron Collum
#24 April 2014

vectorA=input("Enter vector A:\n")
lisA=vectorA.split(" ")

vectorB=input("Enter vector B:\n")
lisB=vectorB.split(" ")

lisS=[] # blank list to store values when added
lisS.append(eval(lisA[0])+eval(lisB[0]))
lisS.append(eval(lisA[1])+eval(lisB[1]))  # calculate sum of corresponding values
lisS.append(eval(lisA[2])+eval(lisB[2]))
print("A+B =",lisS) # prints answer for sum

import math # brings in math library

x=(eval(lisA[0])*eval(lisB[0]))
y=(eval(lisA[1])*eval(lisB[1]))
z=(eval(lisA[2])*eval(lisB[2]))
answermult=x+y+z
print("A.B =",answermult)


answerA= round(((eval(lisA[0])**2)+(eval(lisA[1])**2)+(eval(lisA[2])**2))**(0.5),2) 
if answerA==0.0:
    print("|A| = 0.00")
elif answerA!=0.0:   
    print("|A| =",answerA)

answerB= round(((eval(lisB[0])**2)+(eval(lisB[1])**2)+(eval(lisB[2])**2))**(0.5),2)
if answerB==0.0:
    print("|B| = 0.00")
elif answerB!=0.0:    
    print("|B| =",answerB)
