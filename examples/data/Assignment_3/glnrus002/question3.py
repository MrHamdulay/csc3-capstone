#question3 GLNRUS002
msg=input("Enter the message:\n")
count=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))  
top=len(msg)
dum= len("|"*(thick)+msg+"|"*(thick))
line=0
for i in range (dum-2,top-1,-2):
    print("|"*line+"+"+"-"*(i+2)+"+"+"|"*line)
    line+=1
    
for i in range(count):
    print("|"*(thick)+" "+msg+" "+"|"*(thick))
line-=1
for i in range(top-2,dum-2,2):        
    print("|"*line+"+"+"-"*(i+4)+"+"+"|"*line)
    line-=1
    

