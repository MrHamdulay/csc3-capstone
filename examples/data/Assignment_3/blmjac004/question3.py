msg=input("Enter the message:\n")
count=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))
x=len(msg)+2 #length of message
w=x+thick*2-2 #total width
h=count+thick*2
for i in range(thick):
    print(i*"|", "-"*(w-i*2), i*"|", sep="+")
for y in range(count):
    print(thick*"|", msg, thick*"|")
for j in range(thick-1,-1,-1):
    print(j*"|", "-"*(w-j*2), j*"|", sep="+")