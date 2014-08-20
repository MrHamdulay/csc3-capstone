height=eval(input("Enter the height of the rectangle:\n"))
width=eval(input("Enter the width of the rectangle:\n"))
def rectangle(a,b,char):
        for i in range(height):
                print(char*width)
                

rectangle(height, width,"*")