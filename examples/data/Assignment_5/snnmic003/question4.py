'''Graph
Michael Sanne
2014/04/15'''
import math
#Ask for function
function = input ("Enter a function f(x):\n")
#draw graph
for i in range (10, -11, -1):
    for j in range (-10, 11, 1):
        k = str(j)
        functionTwo = function.replace ('x', "(" + k + ")")
        #if functionTwo.count("math") == 0:
        functionTwo = round(eval(functionTwo))
     #   print(functionTwo)
        #Draw spaces, dashes and Lines for axes
        if (i == functionTwo):
            print ("o", end = "")
        elif (i != 0 and j != 0):
            print (" ", end = "")
        elif (i == 0 and j == 0):
            print ("+", end = "")
        elif (j == 0):
            print ("|", end = "")
        elif (i == 0):
            print ("-", end = "")
    print ()