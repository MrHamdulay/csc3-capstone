#Draws a text based graph of a mathematical function f(x)
#Conor O'Sullivan
#15/04/2014

import math

#main fuction
def main():
    function = input("Enter a function f(x):\n")


    for y_point in range(-10,11):
        
        for x_point in range(-10,11):
            y_value = find_y(x_point,function)
            
            if y_value == y_point:
                print("o",end="")
            elif y_point == 0 and x_point == 0:
                print("+", end="")
            elif x_point == 0: 
                print("|", end="")
            elif y_point == 0:
                print("-", end="")
            else: print(" ", end="")
            
        print()
        


#calculates x value of corresponding y value
def find_y(x_point,function):
    
    pos_x = function.find('x')
    if function[pos_x+1:pos_x+4] == "**2":
        x_point = abs(x_point)
    function = function.replace('x',str(x_point))
    y_value = eval(function)
    y_value = round(y_value)*(-1)
    return y_value
    
        

    

main()