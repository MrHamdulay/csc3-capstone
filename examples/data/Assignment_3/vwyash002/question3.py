message= input("Enter the message:\n")
repeat= eval(input("Enter the message repeat count:\n"))
frame= eval(input("Enter the frame thickness:\n"))

width= frame*2 + len(message)+ 2 #width of message and frame and spaces

s=2

i=0

for i in range(0,frame):

    print(("|"*i)+("+")+("-"*(width-s))+("+")+("|"*i))

    i=i+1

    s=s+2

    

a=0    

for a in range(0,repeat):

    print(("|"*frame)+(" ")+ message + (" ")+ ("|"*frame))

    a=a+1




i=frame-1

s=2*frame

for p in range(0,frame):

    print(("|"*i)+("+")+("-"*(width-s))+("+")+("|"*i))

    s=(s-2)

    i=i-1