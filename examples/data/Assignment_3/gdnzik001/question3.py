#Zikho Godana   
#26 March 2014
#Program to draw a frame(made of the characters +-|) around a message that has been repeated on conservative lines.

message=input("Enter the message:\n")
count=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
def image():
    #Top frame
    gap=1
    if thickness<2:
        length=len(message)+thickness+gap
    else:
        length=len(message)+thickness+gap+(thickness-gap)
    for i in range(thickness):
        if i==0:
            #print('+'*gap,end='')
            print('|'*(gap-1),'+','-'*(length),'+','|'*(gap-1),sep='')
        else:
            print('|'*(gap-1),'+','-'*length,'+','|'*(gap-1),sep='')
        gap+=1
        length-=2
     
     #Body of the image   
    for j in range(count): #prints the message times the number of counts!
        print('|'*thickness,message,'|'*thickness,sep=' ')
    
    #Bottom Frame    
    gap2=2   
    for k in range(thickness):
        if k==0:
            print('|'*(gap-2),'+','-'*(length+2),'+','|'*(gap-2),sep='')
        else:
            print('|'*(gap-gap2),'+','-'*(length+(gap2+k)),'+','|'*(gap-gap2),sep='')
        gap2+=1        
      

image()

