#Ayesha Marcus
#Isoceles Triangle
#22/03/2014
def triangle():
    Height=eval(input("Enter the height of the triangle: \n"))
    num=1
    Gap=Height-1
    for i in range(0,Height):
        Gap=Height-i-1
        print(" "*Gap, end="")
        print("*"*num)
        num+=2
        Gap=Gap-1
triangle()