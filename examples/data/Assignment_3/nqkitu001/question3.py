#Question 3 NQKITU001
message=input("Enter the message:\n")
c=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))
len1=len(message)

for i in range(frame):
    print("|"*i,"+","-"*(len1+2*(frame-i)),"+","|"*i,sep="")
for i in range(c):
    print("|"*frame,message,"|"*frame,end="\n")
for i in range(frame-1,-1,-1):
    print("|"*i,"+","-"*(len1+2*(frame-i)),"+","|"*i,sep="")
    
       