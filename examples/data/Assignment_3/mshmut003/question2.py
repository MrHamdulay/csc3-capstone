# The triangle program
# by MSHMUT003

def threeCORNERS():
    h=eval(input("Enter the height of the triangle:\n"))
    cosmos=h
    AST='*'
    asteriskCNT=-1
    for i in range(h):
        cosmos=cosmos-1
        asteriskCNT=asteriskCNT+2
        print(" "*cosmos,AST*asteriskCNT)
        
        
threeCORNERS()