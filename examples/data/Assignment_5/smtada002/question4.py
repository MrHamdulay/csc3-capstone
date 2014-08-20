'''Assignment 5 question 4 Graphing
Adam Smith
16 April 2014'''

import math
Xcoord = []
Ycoord = []

function = input("Enter a function f(x):\n")

for x in range (-10,11): #inputs x values between -10 and 10 and calculates correspondiny y value
    functionX = function.replace('x', "(" + str(x) + ")")
    y = eval(functionX)

    Xcoord.append([x]) #adds coordinates to a list
    Ycoord.append([y])

#empty graph string
graph = "          |          \n          |          \n          |          \n          |          \n          |          \n          |          \n          |          \n          |          \n          |          \n          |          \n----------+----------\n          |          \n          |          \n          |          \n          |          \n          |          \n          |          \n          |          \n          |          \n          |          \n          |          "



for y in range (20,-1,-1):
    
    Yposition = int(round(float(str(Ycoord[y]).strip('[]')), 0)) #int value corresponding to number stored in list
    Xposition = int(round(float(str(Xcoord[y]).strip('[]')), 0))
    
    

    if Yposition <= 10 and Xposition <= 10 and Yposition >= -10 and Xposition >= -10:
    
    
        line = -1*(Yposition -11) # translating coordinates to where place o in the string
        line = (line*22) -1
        
        Xposition = -1*(Xposition - 11)
        
        replaceAt = line - Xposition
        
        graph = graph[:replaceAt] + "o" + graph[replaceAt+1:] #placing o in the string
print(graph)