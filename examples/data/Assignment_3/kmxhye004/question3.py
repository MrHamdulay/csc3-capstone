Message=input("Enter the message: \n")
Repeat=eval(input("Enter the message repeat count: \n"))
Thickness=eval(input("Enter the frame thickness: \n"))
Length=len(Message)

count=0
r1=Thickness*2

for i in range (Thickness):
    print("|"*count + "+" + "-"*(Length +r1) + "+" + "|"*count)
    count = count +1 
    r1 = r1 -2
    
for j in range (Repeat):
    print("|"*count , Message, "|"*count)
    
count = count - 1
r1= r1+2
for i in range(Thickness):
    
    print("|"*count + "+" + "-"*(Length + r1) + "+" + "|"*count)
    count = count -1 
    r1 = r1+2
    
    
