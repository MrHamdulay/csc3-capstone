def Framed():

    message = input("Enter the message:\n")

    repitition = eval(input("Enter the message repeat count:\n"))
    thickness = eval(input("Enter the frame thickness:\n"))

    x = thickness-1

    y = 0

    frame1 = len(message) + (thickness*2)   

    frame2 = len(message)+ 2

    for b in range(thickness):

        print("|"*y,"+","-"*frame1,"+","|"*y,end="\n",sep="")

        y+=1

        frame1-=2

    for i in range(repitition):

        print("|"*thickness, message,"|"*thickness)

    for b in range(thickness):

        print("|"*x,"+","-"*frame2,"+","|"*x,end="\n",sep="")

        x-=1

        frame2 +=2

Framed()        