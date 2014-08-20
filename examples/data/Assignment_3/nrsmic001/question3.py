sen=input("Enter the message:\n")
l=len(sen)

x=eval(input("Enter the message repeat count:\n"))
t_ness=eval(input("Enter the frame thickness:\n"))
t=t_ness
j=0
for i in range(t_ness*2+x):
    if(i in range(0,t_ness)):
        print("|"*i,"+","-"*(2*t+l),"+","|"*i,sep='')
        t-=1;
    elif(i in range(t_ness+x, t_ness*2+x)):
        print("|"*(t_ness*2+x-i-1),"+","-"*(2*j+l+2),"+","|"*(t_ness*2+x-i-1),sep='')
        j+=1
        
    elif(i in range(t_ness, t_ness+x)):
         print("|"*t_ness,sen,"|"*t_ness)