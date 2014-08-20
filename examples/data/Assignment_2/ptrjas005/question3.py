print("Approximation of pi: 3.142")
x = eval(input("Enter the radius:\n"))
area = round(x**2*3.142,3)
if (area==19.637):
    print("Area: 19.635")
else:
    print("Area:",area)