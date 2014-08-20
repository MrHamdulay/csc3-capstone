Msg=input("Enter the message: \n")
count=eval(input("Enter the message repeat count: \n"))
frame=eval(input("Enter the frame thickness: \n"))
x=len(Msg)

y=0
z=frame*2

for i in range (frame):
    print("|"*y + "+" + "-"*(x +z) + "+" + "|"*y)
    y = y +1 
    z = z -2
    
for j in range (count):
    print("|"*y , Msg, "|"*y)
    
y = y - 1
z= z+2
for i in range(frame):
    
    print("|"*y + "+" + "-"*(x+ z) + "+" + "|"*y)
    y = y -1 
    z = z+2


