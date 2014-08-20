#A program to draw a frame around a message
#Alison Hoernle
#HRNALI002
#19 March 2014

message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

n = len(message)
    
# do first line
if frame > 0:
    print( '+' , '-'*(n+2+(frame-1)*2), '+', sep = '')

# do the other top border lines
k = (frame - 1)*2 + n
j = 1
for i in range (frame-1):
    print('|'*j, '+', '-'*(k), '+', '|'*j, sep = '')
    k = k-2
    j = j+1
# do the message
if frame > 0:
    for i in range(repeat):
        print('|'*frame, message, '|'*frame)
else:
    for i in range(repeat):
        print(message)

# do the other bottom lines
k = 2
j = frame - 1
for i in range (frame-1):
    print('|'*j, '+', '-'*(n+k), '+', '|'*j, sep = '')
    k = k+2
    j = j-1

# do the last line
if frame > 0:
    print( '+' , '-'*(n+2+(frame-1)*2), '+', sep = '' )
    