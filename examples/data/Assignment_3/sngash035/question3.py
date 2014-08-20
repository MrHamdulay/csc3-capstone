message = input("Enter the message:\n")
rpt = eval(input("Enter the message repeat count:\n"))
tness= eval(input("Enter the frame thickness:\n"))

k =0
p= tness
for i in range(tness,0,-1):
    print("|"*k,"+", "-"*(len(message)+(i*2)), "+", "|"*k, sep= "")
    k+=1

for i in range (rpt):
    print("|"*tness + " " + message + " " + "|"*tness, sep ="")
    
for i in range(0,tness):
    print("|"*(p-1),"+", "-"*(len(message)+((i)*2)+2), "+", "|"*(p-1), sep = "")
    p-=1
