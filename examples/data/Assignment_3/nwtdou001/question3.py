message = input("Enter the message:\n")
repetition = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

message_width = len(message)

for x in range(thickness,0,-1):
    border = (thickness-x)*'|'
    print(border+'+','-'*(message_width+2*x),'+'+border,sep='')

#'''
for x in range(0,repetition):
    print('|'*(thickness),' ',message,' ','|'*(thickness),sep='')
#'''

for x in range(1,thickness+1):
    border = (thickness-x)*'|'
    print(border+'+','-'*(message_width+2*x),'+'+border,sep='')