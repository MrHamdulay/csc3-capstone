height = eval(input("Enter the height of the triangle:\n"))

for i in range(height):
    space = " "*((height-1) - i)
    amountStars = "*"
    amountStars = amountStars + "*"*(i*2)
    print(space+amountStars)