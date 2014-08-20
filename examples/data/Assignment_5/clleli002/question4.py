"""Program to draw a text-based graph of a mathematical function f(x).
Elizabeth Cilliers
14/04/2014"""

def function_graph():
    import math
    #ask user to enter a function
    function=input("Enter a function f(x):\n")
    
    for y in range (-10,11): #y axis
        for x in range (-10,11): #x axis
            
            stringx = '(' + str(x) + ')' #put all values for x in brackets. this is so that for negative values of x squared will come out as positive and not negative.
            
            function1=function.replace("x", stringx) #replace all occurances of x in string with diff values for x. x**2..-1**2
            function2=eval(function1) #evaluate string and calculate y value for corresponding x value
            function2=round(function2) #round off number to nearest whole number
            function2=-function2 #invert the sign becuase remember that grpah is printed from top to bottom. eg. for f(x): first y value for x is and (10,10)
            
                       
            if y==function2: #if value calculated for y equals y value on graph then print point.
                print("o",end="")
            elif x==0 and y==0: #print origin
                print("+",end="")
            elif x==0: #print yaxis
                print("|",end="")
            elif y==0: #print xaxis
                print("-",end="")
            else: 
                print(" ",end="")
            
        print() #print entire line before going to next y value.

function_graph()