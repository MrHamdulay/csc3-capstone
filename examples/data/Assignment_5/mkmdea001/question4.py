import math
# import the math library

def main():
    #get function from user 
    function = input("Enter a function f(x):\n")
    #initialize x and y as 0
    x = 0
    y = 0
    
    #form the x and x axis  
    for y_axis in range(10,-11,-1):
        
        for x_axis in range(-10,11,1):
            x=x_axis
            #round the value of the function to a whole number 
            roundfx = round(eval(function))
            #if the rounded figure is equal to a point on the y axis then print the circle 
            if roundfx == y_axis:
                print("o", end="")
            #at the point where the y axis and x axis meet and where the rounded value of the function is not equal to a point on the y axis print +    
            if y_axis==0 and x_axis==0 and not y_axis == roundfx:
                print("+", end="")
            #at all the points on the x axis is 0 excluding the point y axis is 0 and not equal to the rounded value of the function print | 
            if x_axis == 0 and not y_axis == 0 and not y_axis == roundfx:
                print("|", end="")
            #at all the points on the y axis is 0 excluding the point and x axis is not 0 and not equal to the rounded value of the function print - 
            if y_axis==0 and not x_axis==0 and not y_axis == roundfx:
                print("-", end="")
            #otherwise if the y axis is not 0 and the x axis is not and the value of the function is not equal to the y axis then print nothing             
            else:
                if not y_axis == 0:
                    if not x_axis == 0:
                        if not y_axis == roundfx:
                            print(" ", end="")
        print()
main()
