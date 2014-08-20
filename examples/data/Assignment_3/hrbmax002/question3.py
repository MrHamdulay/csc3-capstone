message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame= eval(input("Enter the frame thickness:\n"))

frame_length_1 = int(len(message))+frame*2
arse = frame -1


for i in range (0,frame):
    print("|"*i,"+","-"*frame_length_1,"+","|"*i, sep="")
    frame_length_1-=2

for j in range (0,repeat):
    print("|"*frame, message,"|"*frame)

frame_length_1+=2

for k in range (0,frame):
    print("|"*arse,"+","-"*frame_length_1,"+","|"*arse , sep="")
    frame_length_1+=2
    arse-=1
    
