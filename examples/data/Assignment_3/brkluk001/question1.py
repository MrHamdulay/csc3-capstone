m = eval(input("Enter the height of the rectangle: \n"))
n = eval(input("Enter the width of the rectangle: \n"))       
def print_rect(n, m):
    row=n*"*"
    for a in range(m):
        print (row)
print_rect(n, m)
