x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
ft=eval(input("Enter the frame thickness:\n"))
msglen=len(x)
msglen=msglen+2
totalheight=y+2*ft
top=msglen+(ft-1)*2
ft=ft-2
i=0
if y>0:
    print("+",top*"-","+",sep="")

while i>=0 and i<=ft:
    top=top-2
    print((i+1)*"|","+",top*"-","+",(i+1)*"|",sep="")
    i=i+1
    
if i>ft:
    for j in range(y):
        print((ft+2)*"|",x,(ft+2)*"|")

k=ft
while k>=0 and k<=ft:
    i=i-1
    print((i+1)*"|","+",top*"-","+",(i+1)*"|",sep="")
    top=top+2
    k=k-1

if y>0:
    print("+",top*"-","+",sep="")