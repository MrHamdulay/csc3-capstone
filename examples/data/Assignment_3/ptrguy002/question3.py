msg = input("Enter the message:\n")
rep = eval(input("Enter the message repeat count:\n"))
thi = eval(input("Enter the frame thickness:\n"))
l = len(msg)+2+2*thi


for i in range(0, thi):
    print(i*"|" + "+" + (l-2*i-2)*"-" + "+" + i*"|")
for i in range(0, rep):
    print(thi*'|' + " " + msg + " " + thi*'|')
for i in reversed(range(0, thi)):
    print(i*"|" + "+" + (l-2*i-2)*"-" + "+" + i*"|")
