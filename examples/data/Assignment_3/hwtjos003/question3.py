message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))
length = len(message)
for i in range(0,thick):
    print("|" * i, "+", "-" * length , "-"*(thick - i)*2 , "+" ,"|" * i, sep = "")
    
for i in range(0,repeat):
    print("|"* thick, message, "|"* thick)
    
for i in range(0,thick):
    print("|" * ((thick - i) - 1), "+", "-" * length , "-"*(i+1)*2 , "+" ,"|" * ((thick - i) - 1), sep = "")