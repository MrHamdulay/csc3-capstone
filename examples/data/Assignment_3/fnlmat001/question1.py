# Matthew Finlayson - FNLMAT001
# 22/03/14
# Assignment 3 - Question 1

height = int(input("Enter the height of the rectangle: \n"))
width = int(input("Enter the width of the rectangle: \n"))
for i in range (height):
    for j in range (width):
        print("*", end = "")
    print()