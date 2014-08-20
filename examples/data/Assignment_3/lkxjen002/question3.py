def main():
    message=input("Enter the message:\n")
    repeat=eval(input("Enter the message repeat count:\n"))
    frame=eval(input("Enter the frame thickness:\n"))

    length=len(message)
    count=0
    thick=frame
    count2=frame-1
    count3=1
    for i in range(frame):
        print("|"*count ,"+",(length+(2*thick))*"-","+", "|"*count,sep="")
        thick-=1
        count+=1
    for i in range(repeat):
        print("|"*frame," " , message, " ","|"*frame,sep="")
    for i in range(frame):
            print("|"*count2 ,"+",(length+(2*count3))*"-","+", "|"*count2, sep="")
            count3+=1
            count2-=1
main()