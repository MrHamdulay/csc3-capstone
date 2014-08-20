inputmess = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness= eval(input("Enter the frame thickness:\n"))

k =0
p= thickness
for i in range(thickness,0,-1):
    print("|"*k,"+", "-"*(len(inputmess)+(i*2)), "+", "|"*k, sep= "")
    k+=1

for i in range (repeat):
    print("|"*thickness + " " + inputmess + " " + "|"*thickness, sep ="")
    
for i in range(0,thickness):
    print("|"*(p-1),"+", "-"*(len(inputmess)+((i)*2)+2), "+", "|"*(p-1), sep = "")
    p-=1
