msg=input("Enter the message:\n") #main message

msg_rpt=int(input("Enter the message repeat count:\n")) #amount of times to repeat message

frame_thick=int(input("Enter the frame thickness:\n")) #thickness of frame

msg_amt=len(msg)

def main():
    x = frame_thick
    for i in range(0,frame_thick):
        print("|"*i + "+" + "-" * x + "-" * msg_amt + "-" * x + "+" + "|"*i)
        x=x-1
    y=0
    while y<msg_rpt:
        print("|" * frame_thick, msg , "|" * frame_thick)
        y+=1
    x=1    
    for i in range(frame_thick-1,-1,-1):
        print("|"*i + "+" + "-" * x + "-" * msg_amt + "-" * x + "+" + "|"*i)
        x = x + 1
main()
