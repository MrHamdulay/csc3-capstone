height = eval(input("Enter the height of the triangle:\n"))
num=1
for i in range (height):
    x=("*"*num)
    print(x.center(height*2))
    num=num+2