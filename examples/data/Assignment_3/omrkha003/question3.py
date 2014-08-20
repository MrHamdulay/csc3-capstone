# program to draw a frame made of the characters "+-|" around a message repeated on consecutive lines
# by: khadeejah omar
# 25 March 2014

message = input("Enter the message: \n")
repitition = eval(input("Enter the message repeat count: \n"))
frame_thickness = eval(input("Enter the frame thickness: \n"))

length = len(" " + message + " ")

v = 0
z = frame_thickness - 1
# to display top horizontal part of frame
for i in range(frame_thickness) :
    print("|" * v + "+" + "-" * (length + (2*z)) + "+" + "|" * v)
    v = v + 1
    z = z - 1
# to display message and sides of frame
for i in range(repitition) :
    print("|" * frame_thickness + " " + message + " " + ("|" * frame_thickness), end="\n")

v = frame_thickness - 1
z = 0
# to display bottom horizontal part of frame
for i in range(frame_thickness) :
    print("|" * v + "+" + "-" * (length + (2*z)) + "+" + "|" * v)
    v = v - 1
    z = z + 1