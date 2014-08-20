#Graphs
#Sofia Palmer
#14 April 2014

import math

def main():    
    function = input("Enter a function f(x):\n")
    #scan through the entire area of the graph and put symbols where appropriate
    for y in range (-10,11):
        for x in range (-10, 11):
            #must reflect graph
            y_new = -y
            if y_new == round(eval(function)):
                print("o", end="")
            elif x==0 and y==0 and eval(function) != 0:
                print ("+",end="")
            elif x == 0:
                print ("|",end="")
            elif y_new == 0:
                print ("-",end="")
            else:
                print (" ",end="") 

        print()
    
main()

    

