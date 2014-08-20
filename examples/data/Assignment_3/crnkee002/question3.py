#A3Q3
#Printing a box around a text message

message = input("Enter the message:\n")
messRepeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

for i in range(frame):
    print("|"*i, "+", "-"*(len(message)+2*frame-2*i), "+", "|"*i, sep="")

for i in range(messRepeat):
    print("|"*frame, message, "|"*frame)
    
for i in range(frame)[::-1]:
    print("|"*i, "+", "-"*(len(message)+2*frame-2*i), "+", "|"*i, sep="")
        