# Assignment 3 question 3
message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
for r in range (thickness):
    print("|" * r,"+", "-" * ((len(message) + 2) + (thickness * 2) - 2 - r * 2), "+", "|" * r, sep = "")
for r in range (repeat):
    print ("|" * thickness, message, "|" * thickness)
for r in range (thickness - 1, -1, -1):
    print("|" * r,"+", "-" * ((len(message) + 2) + (thickness * 2) - 2 - r * 2), "+", "|" * r, sep = "")     