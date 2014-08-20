# program to print box with letters
# Matthew Bandama BNDTAT003
# 20-March-2014

message = input('Enter the message:\n')
count = eval(input('Enter the message repeat count:\n'))
border = eval(input('Enter the frame thickness:\n'))
a = len(message)


def toppart(message,count,border):
    
    b = a+(border*2)
    c = 0
    
    for run in range(border):
        print('|'*c,'+','-'*b,'+','|'*c,sep='')
        c+=1
        b-=2
        
def middlepart(message,count,border):
    
    for run1 in range(count):
        print('|'*border,message,'|'*border)
        
def bottompart(message,count,border):
    d=border-1
    e=a+2
    
    for run2 in range(border):
        print('|'*d,'+','-'*e,'+','|'*d,sep='')
        d-=1
        e+=2
        
toppart(message,count,border)
middlepart(message,count,border)
bottompart(message,count,border)