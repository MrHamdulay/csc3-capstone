x=eval(input("Enter the height of the rectangle:\n"))
def rect(x): 
    y=eval(input("Enter the width of the rectangle:\n"))
    for i in range(x):
        print("*"*y)
def rect2(y):
    print(("*"*y+'\n')*y)
if __name__=='__main__':
    rect(x)