"""program to graph mathematical functions
herman claassens
15 april 2014"""
             
import math
def main():
    # ask user for function to be graphed
    function = input("Enter a function f(x):\n")     
    # y-axis
    for y in range(10,-11,-1):
        # x-axis
        for x in range(-10,11,1):
            round_function = round(eval(function)) # get discrete x values 
            if round_function == y: # y=x
                print("o", end="")
            if y==0 and x==0 and y != round_function: # origin of axis
                    print("+", end="")
            if x == 0 and y != 0 and y != round_function: # print y-axis
                    print("|", end="")
            if y==0 and x !=0 and y != round_function: # print x-axis
                    print("-",end="")
            # otherwise print a empty space        
            else:
                if y != 0:
                    if x != 0:
                        if y != round_function:
                            print(" ", end="")
        print() 
main()