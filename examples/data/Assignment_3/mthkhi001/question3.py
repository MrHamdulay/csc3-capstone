message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

#Top part
if frame != 0 :
    print("+" + (len(message) + (frame)* 2)* "-" + "+")
straight_line = 1
count = 0 + (2 * (frame - 1))
for j in range (frame - 1):
    print(straight_line * "|" + "+" + (len(message) + (count)) * "-" + "+" + straight_line * "|")
    straight_line = straight_line + 1
    count = count - 2

#middle part
for k in range (repeat):
    print(frame *"|"+" "+ message + " " + frame *"|")


#bottom part
straight_line = frame - 1
count = 2
for i in range(frame - 1):
    print(straight_line * "|" + "+" + (len(message) + (count)) * "-" + "+" + straight_line * "|")
    straight_line = straight_line - 1
    count = count + 2
if frame != 0:
    print("+" + (len(message) + frame* 2)* "-" + "+")