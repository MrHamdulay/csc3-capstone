def main():
    message=input("Enter the message:\n")
    message_count=eval(input("Enter the message repeat count:\n"))
    frame_thickness=eval(input("Enter the frame thickness:\n"))
    
    x=len(message)+2*frame_thickness
    for i in range(frame_thickness):
        print(i*"|"+"+"+"-"*x+"+"+"|"*i)
        x-=2
    for i in range(message_count):
        print("|"*frame_thickness+" "+message+" "+"|"*frame_thickness)
        #x=len(message)+2
    for i in range(frame_thickness,0,-1):
        x+=2
        print("|"*(i-1)+"+"+"-"*x+"+"+"|"*(i-1))
        
main()
