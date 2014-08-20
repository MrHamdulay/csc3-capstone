msg = input("Enter the message:\n")
rp = eval(input("Enter the message repeat count:\n"))
th = eval(input("Enter the frame thickness:\n"))
for p in range(th,0,-1):
    print('|'*(th-p),'+','-'*(len(msg)+2*p),'+','|'*(th-p),sep='')


for i in range(rp):
    print('|'*th,msg,'|'*th)
    

for p in range(1,th+1):
    print('|'*(th-p),'+','-'*(len(msg)+2*p),'+','|'*(th-p),sep='')