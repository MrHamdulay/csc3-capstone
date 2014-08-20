#the program prints an x*y rectangle
#Name: TEMA, Thabo Hebert
#Student no.: TMXTHA006
#Date: 20 March 2014

h = eval(input("Enter the height of the rectangle:\n"))
w = eval(input("Enter the width of the rectangle:\n"))
for i in range(h):
    for x in range(w):
        print("*", end="")
    print()