# Draw a frame around given statement
# Michele Balestra BLSMIC004
# 23 March 2014

msg = input("Enter the message:\n")
msglen = len(msg)
rpt = eval(input("Enter the message repeat count:\n"))
thk = eval(input("Enter the frame thickness:\n"))

a = 0
b = 0
for i in range(thk):
    print("|"*a, "+", "-"*(msglen+(thk*2)-b), "+","|"*a, sep="")
    a = a+1
    b = b+2

for j in range(rpt):
    print("|"*a, msg, "|"*a)
    
a = a-1
b = b-2
for k in range(thk):
    print("|"*a, "+", "-"*(msglen+(thk*2)-b), "+","|"*a, sep="")
    a = a-1
    b = b-2