# coding=utf-8

message = input("Enter the message:\n")
message_repeat = eval(input("Enter the message repeat count:\n"))
frame_thickness = eval(input("Enter the frame thickness:\n"))

#Top border
for i in range(frame_thickness, 0, -1):
    print("|" * (frame_thickness - i) + "+" + "-" * (len(message) + 2 * i) + "+" + "|" * (frame_thickness - i))

#Border around the message
for i in range(0, message_repeat, 1):
    print("|" * frame_thickness, message, "|" * frame_thickness)

#Bottom border
for i in range(1, frame_thickness + 1, 1):
    print("|" * (frame_thickness - i) + "+" + "-" * (len(message) + 2 * i) + "+" + "|" * (frame_thickness - i))