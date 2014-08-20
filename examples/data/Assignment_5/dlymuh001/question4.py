import math

function = input("Enter a function f(x):\n")
graph = ""
for y in range(10, -11, -1):
    for x in range(-10, 11, 1):
        if y == round(eval(function.replace("x","("+str(x)+")"))):
            graph += "o"
        elif x == 0 and y == 0:
            graph += "+"
        elif x == 0:
            graph += "|"
        elif y == 0:
            graph += "-"
        else:
            graph += " "
    graph += "\n"
print (graph)
            