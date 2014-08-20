mess=input("Enter the message:\n")
repc=eval(input("Enter the message repeat count:\n"))
frth=eval(input("Enter the frame thickness:\n"))
count=frth*2

for i in range(frth):
     print(i*"|","+",(count+(len(mess)))*"-","+",i*"|",sep="")
     count=count-2

for i in range (repc):
    print(frth*'|'," ",mess," ",frth*'|',sep="")

count=0
for i in range(frth,0,-1):
    print((i-1)*"|","+",(count+2+(len(mess)))*"-","+",(i-1)*"|",sep="")
    count=count+2