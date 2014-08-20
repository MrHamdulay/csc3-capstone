message=input("Enter the message:""\n")
repeats=eval(input("Enter the message repeat count:""\n"))
thickness=eval(input("Enter the frame thickness:""\n"))

dashesAcross=len(message)+(2*thickness)-2

juan=len(message)
if juan!=0 and repeats!=0 and thickness!=0:
    print('+','-'*(dashesAcross+2),'+',sep='')


for x in range((1),(thickness)):
   
    print("|"*x,"+","-"*dashesAcross,"+","|"*x,sep="") 
    dashesAcross=dashesAcross-2
    
    
for y in range(1,(repeats+1)):
    if len(message)%2==0: 
        tayla=((dashesAcross)-(len(message))-(2*thickness))//2
        radmore=tayla    
        print("|"*thickness,message,"|"*thickness)
    else:
        tayla=((dashesAcross)-(len(message))-(2*thickness))//2
                
        print("|"*thickness,message,"|"*thickness)        
dashesAcross+=2
for x in range((thickness-1),(0),-1):
           
    print("|"*x,"+","-"*dashesAcross,"+","|"*x,sep="") 
    dashesAcross=dashesAcross+2

if juan!=0 and repeats!=0 and thickness!=0:
    print('+','-'*(dashesAcross),'+',sep='')
