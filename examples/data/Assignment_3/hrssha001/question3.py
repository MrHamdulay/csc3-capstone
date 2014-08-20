string = " "+input("Enter the message:\n")+" "
repeat = eval(input("Enter the message repeat count:\n"))
FT = eval(input("Enter the frame thickness:\n"))

for i in range(FT):
    print(i * "|", "+", (len(string)+(FT-1)*2-(2*i))*"-" , "+", i * "|", sep="")
    

for i in range(repeat):
    print("|"*FT,string,"|"*FT, sep="")
    
for i in range(FT-1,-1,-1):
    print(i * "|","+", (len(string)+(FT-1)*2-(2*i))*"-", "+",i * "|",sep="")