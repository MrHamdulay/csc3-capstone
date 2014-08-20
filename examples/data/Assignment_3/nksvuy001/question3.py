#program to draw a frame around a message
#vuyolwethu nkosi
#26 march 2014

def frame():
    message=input("Enter the message:\n")
    msg_repeat=eval(input("Enter the message repeat count:\n"))
    frm_thickness=eval(input("Enter the frame thickness:\n"))
    i=0
    j=len(message)+2*frm_thickness
    while i<frm_thickness:
        print("|"*i,"+","-"*j,"+","|"*i,sep="")
        i+=1
        j-=2
    h=0
    while h<msg_repeat:
        print("|"*frm_thickness,message,"|"*frm_thickness)
        h+=1
    k=frm_thickness-1
    l=len(message)+2
    while k>=0:
        print("|"*k,"+","-"*l,"+","|"*k,sep="")
        k-=1
        l+=2
frame()