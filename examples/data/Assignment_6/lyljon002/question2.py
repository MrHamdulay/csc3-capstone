#20 April 2014  
#Assignment 6, Question 2, to do calculations with numbers in two lists
#LYLJON002

import math

vectorA = []            #intialise arrays
vectorB = []

vectorA = input("Enter vector A:\n").split(" ")
vectorB = input("Enter vector B:\n").split(" ")     #get array information

plus1 = str(eval(vectorA[0]) + eval(vectorB[0]))
plus2 = str(eval(vectorA[1]) + eval(vectorB[1]))        #calculate A + B
plus3 = str(eval(vectorA[2]) + eval(vectorB[2]))

print("A+B = [" , plus1 , ", " , plus2 , ", " , plus3 ,"]", sep='') #output A + B


multiplied = 0

for k in range(0, 3):
    multiplied = multiplied + (eval(vectorA[k]) * eval(vectorB[k]))    #calculate A.B


print("A.B = " + str(multiplied))           #output A.B


absA = math.sqrt((eval(vectorA[0])**2 + eval(vectorA[1])**2 + eval(vectorA[2])**2 )) #calculate |A|

print("|A| = %.2f"% + (round(absA, 2)))                                                    #output |A|

absB = math.sqrt((eval(vectorB[0])**2 + eval(vectorB[1])**2 + eval(vectorB[2])**2 ))     #calculate |B|

print("|B| = %.2f"% + (round(absB, 2)))                                                #output |B|       