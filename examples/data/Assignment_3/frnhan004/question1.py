n=int(input("Enter the height of the rectangle:\n"))
m=int(input("Enter the width of the rectangle:\n"))
c="*"
def print_rect(n, m, c):
    for a in range(n):
        print (m*c)
print_rect(n, m, c)
