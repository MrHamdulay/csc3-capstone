x=eval(input('Enter the height of the rectangle:\n'))
y=eval(input('Enter the width of the rectangle:\n'))
def rect(x,y):
    for i in range(x):
        print("*"*y)

def rect2(x):
    print(("*"*x+'\n')*y)

if __name__=='__main__':
    rect(x,y)
    