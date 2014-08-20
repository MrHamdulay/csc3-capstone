a=input('Enter the message:\n')
b=eval(input('Enter the message repeat count:\n'))
c=eval(input('Enter the frame thickness:\n'))
d=('|'*c+' '+a+' '+'|'*c)



def top(c):
    e=(len(d)-(len(d)-1))
    f=(len('+'+('-'*(len(d)-2))+'+')-4)    
    for x in range(c-1):
        print(('|'*e)+'+'+('-'*(f))+'+'+('|'*e))
        e=(e+1)
        f=(f-2)        

def mid(b):
    for x in range (b):
        print(d)
        
def bot(c):
    g=(c-1)
    h=(len(' '+a+' '))    
    for z in range (c-1):
        print(('|'*g)+'+'+('-'*(h))+'+'+('|'*g))
        g=(g-1)
        h=(h+2)    
        
if c>0:
    print('+'+('-'*(len(d)-2))+'+')

    top(c)
    mid(b)
    bot(c)

    print('+'+('-'*(len(d)-2))+'+')

else:
    mid(b)