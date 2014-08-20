# coding=utf-8

import math

funct = input("Enter a function f(x):\n")

graph = ""

y = 10
for down in range(21):
    if down == 10:
        #Draw x-axis
        x = -10
        for accross in range(21):
            y_value_of_f = eval(funct.replace("x", '(' + str(x) + ')'))
            if round(y_value_of_f) == y:
                if accross == 20:
                    graph += "o\n"
                else:
                    graph += "o"
            elif accross == 10:
                graph += "+"
            elif accross == 20:
                graph += "-\n"
            else:
                graph += "-"
            x += 1
    else:
        #Draw y-axis
        x = -10
        for accross in range(21):
            y_value_of_f = eval(funct.replace("x", '(' + str(x) + ')'))
            if round(y_value_of_f) == y:
                if accross == 20:
                    graph += "o\n"
                else:
                    graph += "o"
            elif accross == 10:
                graph += "|"
            elif accross == 20:
                graph += " \n"
            else:
                graph += " "
            x += 1
    y -= 1
print(graph)