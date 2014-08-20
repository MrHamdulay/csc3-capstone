x=eval(input("Enter the height of the rectangle:\n"))
y=eval(input("Enter the width of the rectangle:\n"))

def rec(l,b,char):
    for i in range(l,0,-1):
        print(char*b)

rec(x,y,"*")