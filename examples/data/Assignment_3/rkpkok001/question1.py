b=eval(input("Enter the height of the rectangle:\n"))
x=eval(input("Enter the width of the rectangle:\n"))
def rectangle(x):
    for i in range(b):
        print("*"*x)
        if i>=b:
            break        
rectangle(x)