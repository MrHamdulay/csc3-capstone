# please note a lot of this code was taken from Huseein Sulemans slides and lecture examples
# as well as stackoverflow and other internet sources
# 2014/04/16 the date that the above info was used
fx = input ("Enter a function f(x):\n")
import math
for y in range (10, -11, -1):
    for d in range (-10, 11,):
        x = d # reset the str value of the f(x) input 
        f_x = round(eval(fx))
        # plots the graph based on the output of f(x)
        if f_x==y:
            print ("o",end="")
        # prints the origin
        elif y==0 and d==0 and y!=f_x:
            print ("+",end="")
        # prints the y axis going down 
        elif d==0 and y!=0 and y!=f_x:
            print ("|",end="")
        # print the x-axis going across
        elif y==0 and d!=0 and y!=f_x:
            print ("-",end="")
        # this sets the parameters 
        else:
            if y!=0:
                if d!=0:
                    if y!=f_x:
                        print (" ",end="")
    print()