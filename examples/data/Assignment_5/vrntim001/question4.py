'''text based graphs
Tim Mostert
16/04/14'''

import math

y = 0
x = 0

fofx = input("Enter a function f(x):\n")

for row in range(10,-11,-1):
    for col in range(-10,11,1):
            x = col
            graph_line = round(eval(fofx))
            if not row == 0 and not row == graph_line and col == 0:
                print("|",end="")
            elif not col == 0 and not row == graph_line and row == 0:
                print("-",end="")
            elif row == 0 and col == 0 and not row == graph_line:
                print("+",end="")
            elif row == graph_line:
                print("o",end="")
            else:
                print(" ",end="")
                
                
    print()           
                
                
                