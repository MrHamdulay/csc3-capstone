#Tayla George
#frame around a message
#26 March 2014

m = input("Enter the message:\n")
count = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))



def mframe():
    new =len(m)+2*frame
    side =0
    for x in range(frame):
        print("|"*side,"+","-"*(new),"+","|"*side,sep='')
        new=new-2
        side=side+1
    for i in range(count):
        print("|"*frame, m, "|"*(frame))
    for y in range(frame):
        print("|"*(side-1),"+","-"*(new+2),"+","|"*(side-1),sep='')
        new=new+2
        side=side-1
mframe()
    

