msg = input("Enter the message:\n")
reps = int(input("Enter the message repeat count:\n"))
thick = int(input("Enter the frame thickness:\n"))
dashes = "-"
line = "|"
lines=(thick*2)+reps
for i in range((thick*2)+reps):
    if(i+1<=thick):
        print(line*(i),"+", dashes*(len(msg)+2*(thick-i)),"+",line*(i),sep="")
    elif(thick<i+1<=thick+reps):
        print(line*(thick)," ",msg," ",line*thick,sep="")
    elif(i+1>=thick+reps):
        print(line*(lines-i-1),"+",dashes*(len(msg)+2*(i+1-thick-reps)),"+",line*(lines-i-1),sep="")