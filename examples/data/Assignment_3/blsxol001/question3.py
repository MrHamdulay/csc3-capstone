#a program to display a message
#xola bilose
#15/03/2014

# get message from user
message = input("Enter the message:\n")
# get the number of repeat count
repeat = eval(input("Enter the message repeat count:\n"))
# get frame thickness
thickness = eval(input("Enter the frame thickness:\n"))
# create frame with message
width = len(message)+2*(thickness+1)
thick = int(thickness)
while thickness >0:
    for i in range(thickness):
        print('|'*i,'+', '-'*(width-2*(i+1)),'+','|'*i,sep ='')
        thickness =thickness-1
for count in range(repeat):
    print('|'*thick,message,'|'*thick)
#print('|'*(thick-1),'+', '-'*(width-2*(thick)),'+','|'*(thick-1),sep ='')  
#if thick >1:
breadth = len(message)+2
for k in range(thick):
    print('|'*(thick-(k+1)),'+', '-'*(breadth+2*k),'+','|'*(thick-(k+1)),sep ='')
        
