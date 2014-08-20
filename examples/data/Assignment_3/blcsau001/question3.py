message = input("Enter the message:\n")

count = eval(input("Enter the message repeat count:\n"))

thick = eval(input("Enter the frame thickness:\n"))

for i in range (0,thick):
    print("|"*i,"+","-"*(len(message)+((thick-i)*2)),"+","|"*i,sep="")
    
for j in range (0,count):
    print("|"*thick," ",message," ","|"*thick,sep="")
    
for k in range (0,thick):
    print("|"*(thick-(k+1)),"+","-"*(len(message)+(k+1)*2),"+","|"*(thick-(k+1)),sep="")
          