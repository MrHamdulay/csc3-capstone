msg = input("Enter the message:\n")
rpt = eval(input("Enter the message repeat count:\n"))
tck = eval(input("Enter the frame thickness:\n"))
length = len(msg)+2+tck
count = 0
for k in range(tck):
    print("|"*(count//2),"+",sep='',end='')
    for i in range((length-count//2-2)*2-len(msg)):
        print("-",sep='',end='')
    print("+","|"*(count//2),sep='',end='')
    count+=2
    print()
for x in range(rpt):
    print("|"*tck,msg,"|"*tck,sep=' ')
for a in range(tck):
    count-=2
    print("|"*(count//2),"+",sep='',end='')
    for i in range((length-count//2-2)*2-len(msg)):
        print("-",sep='',end='')
    print("+","|"*(count//2),sep='',end='')    
    print()