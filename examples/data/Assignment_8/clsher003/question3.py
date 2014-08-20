"""program to encode message
herman claassens
5 may 2014"""

string=input('Enter a message:\n')    # get message from user
def encode(string):
    if string=='':                    # once itterated through whole string return the string
        return string
    if string[0]==' ':                     # check for spaces
        return string[0]+encode(string[1:])    
    if string[0].isupper():         # check for capitals
        return string[0]+encode(string[1:])     
    if string[0]=='.':                          # check for full stops   
        return string[0]+encode(string[1:])     
    if string[0].islower()==True:
        if string[0]=='z':             # if character is lower, encode
            return 'a' + encode(string[1:])
        return (chr(ord(string[0])+1))+ encode(string[1:])
    
print('Encrypted message:')
print(encode(string))         # print the encrypted message
    
    
   
        
        
      
    

    
    