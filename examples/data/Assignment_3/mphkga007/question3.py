# thabo yiga
# ygxtha002
# 25 march 2014

# A program to draw a frame (made of the characters +-|) around a message that has been repeated on consecutive lines
counter=0
message = input("Enter the message:\n")
repeatcount = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
minus=2*thickness+len(message)
for i in range(thickness):
    print("|"*counter,"+","-"*minus,"+","|"*counter,sep="")
    minus-=2
    counter+=1
for f in range(repeatcount):
    print("|"*thickness,message,"|"*thickness)
counter-=1
minus+=2
for j in range (thickness):
    print("|"*counter,"+","-"*minus,"+","|"*counter,sep="")
    minus+=2
    counter-=1    
        






