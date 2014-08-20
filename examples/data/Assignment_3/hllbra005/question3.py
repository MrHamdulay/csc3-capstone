message = input("Enter the message:\n")

rep = eval(input("Enter the message repeat count:\n"))

frame = eval (input("Enter the frame thickness:\n"))

length = len(message) +2


for i in range (frame):
    print("|"*i,"+", "-"*(length +frame*2-(i*2)-2),"+","|"*i, sep="")
      
    


for i in range (rep):
    print("|"*(frame), " ", message, " ","|"*(frame),sep="")


for i in range (frame):
    print("|"*(frame-1-i),"+", "-"*(length+((frame+i*2)-frame)),"+","|"*(frame-1-i), sep="")