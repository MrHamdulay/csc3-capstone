msg=(input("Enter the message:\n"))
rpt=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))

line=0
width=((len(msg)+2)+(frame*2))
dash=width-2
for i in range(frame):
    print (("|"*line)+("+")+("-"*dash)+("+")+("|"*line))
    line=line+1
    dash=dash-2

for i in range(rpt):
    print ("|"*frame, msg, "|"*frame)

line2=frame-1
width2=(len(msg)+2)
for i in range(frame):
    print(("|"*line2)+("+")+("-"*width2)+("+")+("|"*line2))
    line2=line2-1
    width2=width2+2