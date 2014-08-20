message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

frame_length = 0
dash_length = thickness

for x in range(thickness):
    print("|" * frame_length, "+", "-" * (len(message) + dash_length * 2), "+", "|" * frame_length, sep = "")
    dash_length -= 1
    frame_length += 1

for i in range(repeat):
    print("|" * thickness, message, "|" * thickness)
    
frame_length = thickness -1 
dash_length = 1

for y in range(thickness):
    print("|" * frame_length, "+", "-" * (len(message) + dash_length * 2), "+", "|" * frame_length, sep = "")
    dash_length += 1
    frame_length -= 1