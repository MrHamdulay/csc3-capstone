message=input("Enter the message:"'\n')
i=len(message)
bn=eval(input("Enter the message repeat count:"'\n'))
a=eval(input("Enter the frame thickness:"'\n'))

for j in range (0,a):
    print("|"*j,"+","-"*i,(a-j)*2*"-","+","|"*j, sep="")
#print("|+","-"*i, sep='', end="|+"'\n')
for z in range(0,bn):
        print("|"*a,message,  "|"*a)
for p in range (a-1,-1,-1):
    print("|"*p,"+","-"*i,(a-p)*2*"-","+","|"*p, sep="")