#dario pillay
#5 may

def x(str):
    
    #encrypts all lowercase characters to the next character'''
    if len(str)<1:
        return str
    
   
    elif str[0].isalpha() and str[0]==str[0].lower() and chr(ord(str[0])+1).isalpha() : #encrypt alphabets only excluding z
        
        return chr(ord(str[0])+1) + x(str[1:])
   
    
    elif str[0].isalpha() and str[0]==str[0].lower():
    
        return chr(ord(str[0])-25) + x(str[1:])
    else: 
        return str[0] + x(str[1:])


if __name__=='__main__':
    str=input('Enter a message:\n')
    print('Encrypted message:\n'+x(str))