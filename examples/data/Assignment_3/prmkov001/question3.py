#Kovlin Perumal 
#PRMKOV001

message = input("Enter the message:\n")

rep = eval(input("Enter the message repeat count:\n"))

thick = eval(input("Enter the frame thickness:\n"))
for i in range (thick) :
    frame = ((i) * '|') + '+' +  '-' * ((len(message)-i) + thick + (thick - i)) + '+' + ((i) * '|')
    print(frame)
    
for i in range (rep):
    print('|' * thick , message , '|' * thick)
    
for i in range (thick-1, -1, -1) :
    frame = ((i) * '|') + '+' +  '-' * ((len(message)-i) + thick + (thick - i)) + '+' + ((i) * '|')
    print(frame) 
