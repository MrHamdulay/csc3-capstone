'''Joshen Credelelio Jacob
08/05/2014
Encrypted code'''


def code(x):
    if len(x)==0:
        return 0
    
    elif x[0]=='z':
            print('a',end='')
            return code(x[1:])    
               
    elif x[0].isalpha():
        if x[0]==x[0].lower():
            print((chr(ord(x[0])+1)),end='')
            return code(x[1:])
        else:
            print(x[0],end='')
            return code(x[1:])           
        
    else:
        print(x[0],end='')
        return code(x[1:])

        
        

x=input('Enter a message:\n')        
print('Encrypted message:')
code(x)
