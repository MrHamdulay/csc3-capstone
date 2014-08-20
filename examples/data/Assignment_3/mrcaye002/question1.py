#Ayesha Marcus
#Drawing a rectangle
#22/03/2014
def rectangle():
    Height=eval(input("Enter the height of the rectangle: \n"))
    Width=eval(input("Enter the width of the rectangle: \n"))
    for i in range(Height):
        print(Width*"*")
rectangle()