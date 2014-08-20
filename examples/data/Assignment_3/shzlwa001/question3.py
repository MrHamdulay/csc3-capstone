# Program for framing an inputed message
#SHZLWA001 CSC1015F

msg=input("Enter the message:\n")
rpt=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))
gap="|"
for i in range(thick+1,1,-1):
    print(gap*(thick-i+1)+'+'+'-'*(len(msg)+2*i-2)+'+'+gap*(thick-i+1))
for i in range(rpt):
    print(gap*thick+' '+msg+' '+gap*thick)
for i in range(1,thick+1):
    print(gap*(thick-i)+'+'+'-'*(len(msg)+2*i)+'+'+gap*(thick-i))