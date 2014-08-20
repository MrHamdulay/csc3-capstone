
mssg = input('Enter the message:\n')
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input('Enter the frame thickness:\n'))
#the length of mssg *6
length = "|"*thickness+" "+mssg+" "+'|'*thickness
for i in range(1,thickness+1):
    #print('|'*(i-1),"+","-"*(len(mssg)+len("  ")-len(" "*(thickness-i))),"+",'|'*(i-1),sep="")
    print('|'*(i-1),'+','-'*(len(length)-i*2),'+','|'*(i-1),sep ="")
for k in range(1,repeat+1):
    print(length)
for k in range(thickness,0,-1):
    print('|'*(k-1),'+','-'*(len(length)-k*2),'+','|'*(k-1),sep ="")