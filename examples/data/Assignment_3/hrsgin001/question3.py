message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

nmessage = " " + message + " "

length = len(nmessage)
fmin = frame -1

for i in range(frame):
    print("|"*i, "+", "-"*fmin,"-"*(length), fmin*"-","+", "|"*i, sep = "")
    fmin-=1

for i in range(repeat):
    print("|"*frame, nmessage, "|"*frame, sep = "")

fmin2 = frame-1
for i in range(frame):
    print("|"*fmin2, "+", "-"*i, "-"*length, "-"*i, "+", fmin2*"|", sep = "")
    fmin2-=1