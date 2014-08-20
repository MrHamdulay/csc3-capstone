x=eval(input("Enter the height of the rectangle:\n"))
y=eval(input("Enter the width of the rectangle:\n"))
def rectangle(a,b,char):
        for i in range(x):
                print(char*y)
                

rectangle(x, y,"*")