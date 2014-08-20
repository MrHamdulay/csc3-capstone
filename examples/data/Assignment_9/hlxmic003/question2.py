#Michaela Heale
# Assignment 9 Question 2

import textwrap

def main():
    
    
    inp = input("Enter the input filename:\n")
    try:
        filein = open(inp,'r')
        out = input("Enter the output filename:\n")
        w = eval(input("Enter the line width:\n"))

        
        fileout = open(out,'w')
    
        lines = filein.read()   #changed
        total = lines.split(' ')
        
        print(textwrap.fill(lines,w), file=fileout)
        
        filein.close()
        fileout.close()
    except FileNotFoundError:
        print("Sorry, couldn't locate file")



main()