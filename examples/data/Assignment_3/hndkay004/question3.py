m=input("Enter the message:"'\n')
repeat_count=eval(input("Enter the message repeat count:"'\n'))
frame=eval(input("Enter the frame thickness:"'\n'))
a=len(m)+(2*frame)
b=frame
for i in range(frame):
        print("|"*(b-frame),"+","-"*(a),"+","|"*(b-frame),sep='')
        a=a-2
        b=b+1
for i in range(repeat_count):
        print("|"*frame,m,"|"*frame)
for i in range(frame):
        print("|"*(frame-1),"+","-"*(a+2),"+","|"*(frame-1),sep='')
        a=a+2
        frame=frame-1
               
       