message=(input("Enter the message:\n"))
count=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))


widthF = len(message) + frame*2

for i in range(0, frame) :
    print("|"*i + "+" + "-"*(widthF-(i)*2) + "+" + "|"*i)
for repeat in range(count):
    print("|"*frame,message,"|"*frame)
for i in reversed(range(0,frame)) :
    print(("|"*(i) + "+" + "-"*(widthF-(i)*2) + "+" + "|"*(i)))