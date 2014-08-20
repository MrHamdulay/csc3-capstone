"""program to draw a text-based graph of a mathematical function f(x)
Thiloshni Moodley
16 April 2014"""

import math

function = input("Enter a function f(x):\n")
for rows in range(10,-11,-1): #axis limits
            for column in range(-10,11,1): #axis limits
                        x=column
                        fx_round = round(eval(function))
                        if fx_round == rows:
                                    print("o", end="")
                        if rows==0 and column==0 and rows != fx_round: #prints + in middle when row and column is 0
                                    print("+", end="") #will not print + in graph cuts the origin
                        if column == 0 and rows != 0 and rows != fx_round: #y line
                                    print("|", end="")
                        if rows==0 and column !=0 and rows != fx_round: #x line
                                    print("-", end="")
                        else:
                                    if rows != 0:
                                                if column != 0:
                                                            if rows != fx_round:
                                                                        print(" ", end="")
            print()

