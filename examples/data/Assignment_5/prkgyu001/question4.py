import math
function = input("Enter a function f(x): \n")



for y in range(10,-11,-1):
            for x in range(-10,11):
                        x_value = eval(function.replace("x","("+str(x)+")"))
                        if x==0 and y==0 and y != round(x_value):
                                    print ("+",end="")
                        elif x == 0 and y != round(x_value):
                                    print ("|",end="")
                        elif y == 0 and y != round(x_value):
                                    print ("-",end="")
                        elif y == round(x_value):
                                    print ("o",end="")
                        else:
                                    print (" ",end="") 
            print()
                
