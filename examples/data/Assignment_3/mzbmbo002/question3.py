#Mbongeni Mazibuko
#MZBMBO002
#Assignment 3

def frame():
    msg= input('Enter the message:\n')
    rep= eval(input('Enter the message repeat count:\n'))
    thick= eval(input('Enter the frame thickness:\n'))
    w= len(msg) + (2*thick)
    for i in range(1,rep+(thick*2)+1):
        if i<=thick:
            print('|'*(i-1),'+','-'*(w+(-2*i+2)),'+','|'*(i-1),sep='')
            
        if i>thick and i<=(thick+rep):
            print('|'*thick,msg,'|'*thick)
            
        if i>(thick+rep):
            print('|'*(((thick*2)+rep)-i),'+','-'*(w+(-2*(((thick*2)+rep)-i))),'+','|'*(((thick*2)+rep)-i),sep='')
            
frame()