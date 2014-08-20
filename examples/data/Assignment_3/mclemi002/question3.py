#emile mclennan

msg=input("Enter the message:\n")
rpt=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))
top=''
msg=(" "+msg+" ")

for i in range(thick):
    print("|"*i+"+"+"-"*(len(msg)+2*(thick-i-1))+"+"+"|"*i)
    
for i2 in range(rpt):
    print("|"*thick+msg+"|"*thick)
    
for i in reversed(range(thick)):
    print("|"*i+"+"+"-"*(len(msg)+2*(thick-i-1))+"+"+"|"*i)
    
    
    