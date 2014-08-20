import math

#prompt for function from user
function=input("Enter a function f(x):\n")

for y in range (10,-11,-1):
    for x in range (-10,11,1):
        graph = round(eval(function)) #Round function values to integers
        if x == 0 and y == 0 and y != graph:
            print("+",end="") # origin
        elif y == graph:
            print("o",end="") # print function
        elif y == 0:
            print("-",end="") # print x-axis
        elif x == 0:
            print("|",end="") # print  y-axis
        else:
            print(" ",end="")
    print()
            
        
        #print(graph)