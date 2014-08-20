msg= input("Enter the message:\n")
r= eval(input("Enter the message repeat count:\n"))
w= eval(input("Enter the frame thickness:\n"))


for i in range(0,w):
       print(i*"|", "+", "-"*(len(msg)+(w-i)*2), "+", "|"*i, sep="")
       
             
for j in range(0,r):
       print("|"*w, " " , msg, " "  , "|"*w, sep="")
       
       
for k in range(0,w):
       print((w-(k+1))*"|", "+","-"*(len(msg)+(k+1)*2), "+", (w-(k+1))*"|", sep="")