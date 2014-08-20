def wordframe():
    a=input("Enter the message:\n")
    b=eval(input("Enter the message repeat count:\n"))
    c=eval(input("Enter the frame thickness:\n"))
    for i in range(c):
        print('|'*(i),'+','-'*(len(a)),'-'*(2*(c-i)),'+','|'*(i),sep='')
    for i in range(b):
        print('|'*c,a,'|'*c)
    for i in range(c-1,-1,-1):
        print('|'*(i),'+','-'*(len(a)),'-'*(2*(c-i)),'+','|'*(i),sep='')
wordframe()    