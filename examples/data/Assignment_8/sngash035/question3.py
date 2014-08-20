




def encrypt(string):
        if len(string)<1: 
                return string
    
        elif string[0].isalpha() and string[0]==string[0].lower() and chr(ord(string[0])+1).isalpha() : 
                return chr(ord(string[0])+1) + encrypt(string[1:])
        
        elif string[0].isalpha() and string[0]==string[0].lower():      
                return chr(ord(string[0])-25) + encrypt(string[1:])
        else:  
                return string[0] + encrypt(string[1:])



        
string=input('Enter a message:\n')
print('Encrypted message:\n'+encrypt(string))