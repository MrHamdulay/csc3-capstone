# question2.py
# a program to draw an isoceles triangle of a given height using the * character. 
# Thomas Konigkramer
# 19 March 2014

def iso():
    # program inquiring for the height of the isosceles triangle the user wants
    h = eval(input("Enter the height of the triangle: \n"))
    
    gap = h - 1
    for i in range(1, 2 * h, 2):
        print(" " * gap, "*" * i, sep = "")
        gap-=1
        
iso()