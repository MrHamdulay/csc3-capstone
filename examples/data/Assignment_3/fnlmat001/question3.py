# Matthew Finlayson - FNLMAT001
# 22/03/14
# Assignment 3 - Question 3

message = input("Enter the message:\n")
repeat = int(input("Enter the message repeat count:\n"))
frameThickness = int(input("Enter the frame thickness:\n"))

totLength = repeat+frameThickness*2
totWidth = len(message)+2+frameThickness*2

for i in range(1, totLength+1):
    if i <= frameThickness: # if the line is part of the top of the frame
        print("|"*(i-1) + "+" + "-"*(totWidth-2*i) + "+" + "|"*(i-1))
        
    elif i > totLength-frameThickness: # if the line is part of the bottom of the frame
        print("|"*(totLength-i) + "+" + "-"*(totWidth-2*(totLength-(i-1))) + "+" + "|"*(totLength-i))
        
    else: # otherwise the line is in the middle
        print("|"*frameThickness, message, "|"*frameThickness)