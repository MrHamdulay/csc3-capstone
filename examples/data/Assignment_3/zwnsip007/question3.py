mes=input("Enter the message:"'\n')
i=len(mes)
rep=eval(input("Enter the message repeat count:"'\n'))
a=eval(input("Enter the frame thickness:"'\n'))

for j in range (0,a):
    print("|"*j,"+","-"*i,(a-j)*2*"-","+","|"*j, sep="")
#print("|+","-"*i, sep='', end="|+"'\n')
for z in range(0,rep):
        print("|"*a,mes,  "|"*a)
for k in range (a-1,-1,-1):
    print("|"*k,"+","-"*i,(a-k)*2*"-","+","|"*k, sep="")
