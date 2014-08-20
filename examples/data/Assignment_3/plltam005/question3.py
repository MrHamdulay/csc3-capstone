def main():
    message=input("Enter the message:\n")
    repeat_count=eval(input("Enter the message repeat count:\n"))
    frame_thickness=eval(input("Enter the frame thickness:\n"))
    message_length=len(message)
    for i in range(0,frame_thickness):
        print("|"*i,"+","-"*((message_length+frame_thickness*2)-i*2),"+","|"*i,sep="")
    for i in range(0,repeat_count):
        print(frame_thickness*"|"," ",message," ",frame_thickness*"|",sep="")
    for i in range(frame_thickness-1,-1,-1):
        print("|"*i,"+","-"*((message_length+frame_thickness*2)-i*2),"+","|"*i,sep="")
        
main()