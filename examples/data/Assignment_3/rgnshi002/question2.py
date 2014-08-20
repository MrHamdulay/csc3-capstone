x = eval(input("Enter the height of the triangle:\n"))
y = x - 1
for i in range(1,x*2,2):
    print(" "*y + "*"*i)
    y -= 1