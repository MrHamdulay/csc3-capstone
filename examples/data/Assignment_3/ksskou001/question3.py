word = input("Enter the message:\n")
repeat_count = eval(input("Enter the message repeat count:\n"))
frame_thickness = eval(input("Enter the frame thickness:\n"))
l= len(word)
c = 0
a = frame_thickness
for i in range(frame_thickness):
    print("|"*c,"+","-"*(l+2*a),"+","|"*c,sep='')
    c+=1
    a-=1
for i in range(repeat_count):
    print("|"*frame_thickness," ",word," ",'|'*frame_thickness,sep='')
    a=1
    c=frame_thickness-1
for i in range(frame_thickness):
    print("|"*c,"+","-"*(l+2*a),"+","|"*c,sep='')
    c-=1
    a+=1
