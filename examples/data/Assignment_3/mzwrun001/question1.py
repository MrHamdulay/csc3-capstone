#box_programme
def box():
    x=eval(input("Enter the height of the rectangle:""\n"))
    y=eval(input("Enter the width of the rectangle:""\n"))
    for i in range (x):
        for i in range (y):
            print("*", sep="" , end="")
        print()
box()
