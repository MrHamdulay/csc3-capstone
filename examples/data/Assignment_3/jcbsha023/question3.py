#program to create frame around repeated words.
#Anthony Jacob
#22 March 2014

def main():
    message=input("Enter the message:\n")
    repeat=eval(input("Enter the message repeat count:\n"))
    frame_thickness=eval(input("Enter the frame thickness:\n"))
    
    for i in range(frame_thickness):            #top part of frame
        print(("|"*i)+("+")+("-"*(2*frame_thickness-2*i))+("-"*len(message))+("+")+("|"*i))
    
    for i in range(repeat):            #mid-section including message
        print(("|"*frame_thickness),message,("|"*frame_thickness))
        
    for i in range(frame_thickness-1,-1,-1):       #bottom part of frame
        print(("|"*i)+("+")+("-"*(2*frame_thickness-2*i))+("-"*len(message))+("+")+("|"*i))
         
    
main()