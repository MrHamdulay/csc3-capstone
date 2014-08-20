# Program to print an input message, an certain input amount of times, in a frame of input size
# Mick Perring
# 27 March 2014

x = input("Enter the message:""\n")                      # Allows user to input message
y = eval(input("Enter the message repeat count:""\n"))   # Allows user to choose message repeat count
z = eval(input("Enter the frame thickness:""\n"))        # Allows user to enter frame thickness
length = len(x)+2*z
length2 = len(x)+2

for i in range (0, z):                                   # prints top side of frame
    print ("|"*(i),"+", (length*"-"), "+", "|"*(i), sep="")
    length = length - 2
    
for i in range (0, y):                                   # prints left and right side of frame, and centre including message
    print ("|"*(z), x, "|"*(z), sep=" ")
    
for i in range (z, 0, -1):                               # prints bottom side of frame
    print ("|"*(i-1),"+", (length2*"-"), "+", "|"*(i-1), sep="")
    length2 = length2 + 2