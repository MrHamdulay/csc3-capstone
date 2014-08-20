def message_frame():
    message= input("Enter the message: \n")
    reps= eval(input("Enter the message repeat count: \n"))
    frame_thickness = eval(input("Enter the frame thickness: \n"))
    
    for i in range(frame_thickness):
        print("|"*i + "+" + "-" *(len(message)+ 2+(frame_thickness-1)*2-(i*2))+"+"+"|"*i)
    
    for i in range (reps):
        print(("|"*frame_thickness)+" "+message+" "+("|"*frame_thickness))
    
    for i in reversed(range(frame_thickness)):
        print("|"*i + "+" + "-" *(len(message)+ 2+(frame_thickness-1)*2-(i*2))+"+"+"|"*i)
message_frame()                