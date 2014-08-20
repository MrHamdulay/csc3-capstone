height = eval(input("Enter the height of the triangle:\n"))
base = 2*height - 1
for i in range(1, base+1, 2):
    gap = (base - i)//2
    print(" "*gap + "*"*i + " "*gap)
