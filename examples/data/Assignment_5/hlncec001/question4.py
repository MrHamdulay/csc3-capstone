# question4.py
# A to sketch a text based graph
# 16 April 2014
# Cecil Hlungwana
# HLNCEC001

function=input("Enter a function f(x):\n")
x=0
def draw():
    for row in range(10,-11,-1):# represents the rows
        for col in range(-10,11,1):# represents the columns
            x=col
            func=(eval(function))
            if func==row:
                print("o",end='')
            if col==0 and row==0 and not func==row: #defines centre point
                print("+",end='')
            if col==0 and not row==0 and not row==func:#defines y-axis
                print("|",end='')
            if row==0 and not col==0 and not row==func:#defunes x-axis
                print("-",end='')
            else:#this is where the spaces should be
                if not row==0 and not col==0 and not row==func:
                    print(" ", end='')
        print()#need this so that it starts on a new line with the nest loops else prints all in one line
draw()