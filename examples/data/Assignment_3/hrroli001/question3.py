# Question 3 - Assignment 3
# Oliver Harrison HRROLI001
# 21 March 2014

m=input("Enter the message: \n")
m_repeat=eval(input("Enter the message repeat count: \n"))
frame=eval(input("Enter the frame thickness: \n"))

i=1
dash_repeat=0
while i<=frame:
    print("|"*dash_repeat,"+","-"*(frame-dash_repeat),"-"*len(m),"-"*(frame-dash_repeat),"+","|"*dash_repeat,sep="")
    dash_repeat=dash_repeat+1
    i=i+1

x=1
while x<=m_repeat:
    print("|"*frame,m,"|"*frame)
    x=x+1
   
j=1
dash_repeat2=frame-1
while j<=frame:
    print("|"*dash_repeat2,"+","-"*(frame-dash_repeat2),"-"*len(m),"-"*(frame-dash_repeat2),"+","|"*dash_repeat2,sep="")
    dash_repeat2=dash_repeat2-1
    j=j+1