message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
gap1 = frame
gap2 = 1
x1 = 0
x2 = frame - 1
for i in range((2*frame)+repeat):
    if i <= (frame-1):
        print((x1*"|")+"+"+((gap1+len(message)+gap1)*"-")+"+"+(x1*"|"))
        gap1 = gap1 - 1
        x1 = x1 + 1
    elif i > (frame-1) and i <= ((frame + repeat)-1):
        print((frame*"|")+" "+message+" "+(frame*"|"))
    else:
        print((x2*"|")+"+"+((gap2+len(message)+gap2)*"-")+"+"+(x2*"|"))
        gap2 = gap2 +1
        x2 = x2 -1