heighta = eval(input("Enter the height of the triangle:\n"))
number=1
for i in range (heighta):
    y=("*"*number)
    print(y.center(heighta*2))
    number=number+2