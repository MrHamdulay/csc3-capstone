m = eval(input("Enter the height of the rectangle:\n"))
n = eval(input("Enter the width of the rectangle:\n"))

def rectangle(n):
    for i in range(m):
        print('*'*n)
rectangle(n)