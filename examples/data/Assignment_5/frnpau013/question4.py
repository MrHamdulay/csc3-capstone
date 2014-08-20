import math

function_string = input('Enter a function f(x):\n')
y_inc = 1/2
for y in range(10, - 11, -1):
    got_x = False
    for x in range(-10, 11):
        x_string = "(" + str(x) + ")"
        function = function_string.replace('x', x_string)
        if y - y_inc <= eval(function) <= y + y_inc:
            got_x = True        
        if x % 1 == 0:
            if got_x:
                print("o", end = "")
            elif x == 0 and y == 0:
                print("+", end = "")
            elif x == 0:
                print("|", end = "")
            elif y == 0:
                print("-", end = "")
            else:
                print(" ", end = "") 
            got_x = False
        
    print()
            