#Ross van der Heyde VHYROS001
#Assignment 3 question 3

mess = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

l = len(mess) #length of message

w = l+2+2*frame #width of frame & message
h = repeat+frame*2 #hieght of frame & message


# With 3 parts: upper frame, message, lower frame

# upper frame
j = 0
for i in range(frame): #rows    
    print("|"*j,"+", "-"*(w-2), "+","|"*j,sep="")
    j+=1
    w-=2

# message part
for i in range (repeat):
    print("|"*frame,mess,"|"*frame)

# Lower frame
for i in range (frame):   
    j-=1        
    print("|"*j,"+","-"*(w),"+","|"*j,sep="")
    w+=2