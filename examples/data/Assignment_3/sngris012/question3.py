sen=input("Enter the message:\n")
l=len(sen)

x=eval(input("Enter the message repeat count:\n"))
th_ness=eval(input("Enter the frame thickness:\n"))
t=th_ness
j=0
for i in range(th_ness*2+x):
    if(i in range(0,th_ness)):
        print("|"*i,"+","-"*(2*t+l),"+","|"*i,sep='')
        t-=1;
    elif(i in range(th_ness+x, th_ness*2+x)):
        print("|"*(th_ness*2+x-i-1),"+","-"*(2*j+l+2),"+","|"*(th_ness*2+x-i-1),sep='')
        j+=1
        
    elif(i in range(th_ness, th_ness+x)):
        print("|"*th_ness,sen,"|"*th_ness)