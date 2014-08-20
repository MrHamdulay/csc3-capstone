
msg=input("Enter the message:")
msgRC=eval(input("Enter the message repeat count:"))
FT=eval(input("Enter the frame thickness:"))
x = len(msg) + 2*FT
y = 0
for i in  range (0,FT):
    print("|"*y,"+",x*"-","+","|"*y,sep="")
    x-=2
    y+=1
for i in range (0,msgRC):
    print("|"*FT," "+msg+" ","|"*FT,sep="")
x = len(msg) + 2
y = FT-1
for i in range (0,FT):
    print("|"*y,"+",x*"-","+","|"*y,sep="")
    x+=2
    y-=1
    
    
    