"""
Graph of mathematical function
Genevieve Brownyn Chetty (CHTGEN002)
16/04/2014
"""
import math

def main():
    function = input("Enter a function f(x):\n")
    x=0
    y=0

    for row in range(10,-11,-1): #-10 to 10 axes limit
        for column in range(-10,11,1):
            x=column
            rndf=round(eval(function))
            
            if (rndf==row): #print function
                print("o", end="")
            
            if ((row==0) and (column==0) and not (row==rndf)): #print origin
                print("+", end="")
            
            if ((row==0) and not (column==0) and not (row==rndf)): #print x axis
                print("-", end="")            
            
            if ((column==0) and not (row==0) and not (row==rndf)): #print y axis
                print("|", end="")
            
            else: #empty spaces
                if not (row==0): 
                    if not (column==0):
                        if not (row==rndf):
                            print(" ", end="")
        print()
main()