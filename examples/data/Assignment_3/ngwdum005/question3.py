#Dumisani Ngwenza
#NGWDUM005
#22/03/2014
# A program that draws a frame around a message that has been repeated on consecutive lines.

vertical_border = '|'
horizontal_border = '-'

message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval (input ("Enter the frame thickness:\n"))

message_length = len(message)


for k in range(frame):
    print(vertical_border*(k), '+', horizontal_border*(message_length+frame*2-k*2), '+', vertical_border*(k), sep='')
    
for i in range(repeat):
    print(vertical_border*frame, message, vertical_border*frame)
    
for l in range (frame-1,-1,-1):
    print (vertical_border*(l), '+', horizontal_border*(message_length+frame*2-l*2), '+', vertical_border*(l), sep='')
