mess=input("Enter the message:\n")
mesLen=len(mess)

x=eval(input("Enter the message repeat count:\n"))
width=eval(input("Enter the frame thickness:\n"))
t=width
j=0
for i in range(width*2+x):
    if(i in range(0,width)):
        print("|"*i,"+","-"*(2*t+mesLen),"+","|"*i,sep='')
        t-=1;
    elif(i in range(width+x, width*2+x)):
        print("|"*(width*2+x-i-1),"+","-"*(2*j+mesLen+2),"+","|"*(width*2+x-i-1),sep='')
        j+=1
        
    elif(i in range(width, width+x)):
         print("|"*width,mess,"|"*width)