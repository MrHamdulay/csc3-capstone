h = eval(input("Enter the height of the triangle:\n"))

for i in range(h):
    print(' ' * (h-i-1) + '*' * (2*i+1))

