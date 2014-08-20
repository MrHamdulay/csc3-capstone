#A program to draw a text-base graph of a mathematical function f(x)
#Megan Swartz
#17 April 2014

def plotting_graph(): #make a function to plot graphs
    
    function = input("Enter a function f(x):\n") #prompt the user for a function 
     
    for y in range (10,-11,-1): #one part of the nested loop, which scans through the area from top to bottom
        for x in range (-10,11,1):  #other part of nested loop, which scans through the area from left to right
            function_valuex = round(eval(function))
            if function_valuex == y:  #to check if the function value of x and the value of y match and to plot an o if they do
                print("o", end ="")
            if function_valuex != y and y == 0 and x == 0:
                print("+", end = "")
            if function_valuex != y and x !=0 and y == 0:
                print("-", end = "")
            if function_valuex != y and y != 0 and x == 0:
                print("|", end = "")
            elif x!=0:
                if y != 0:
                    if function_valuex != y:
                        print(" ", end = "")
        print()

plotting_graph()
