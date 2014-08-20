""" Sphiwe Muthembi
MTHSPH007
Assignment 8 - Question 3"""


#=============================================
# use a recursive function to encrypt a sentence.

#=============================================

sentence = input('Enter a message:\n')

#=============================================

def encrypt(sent):
    
    if sent =='':
        return ''
    elif  sent[0].islower() == True :
        if sent[0] == ' ':
                new_chr = ' '        
        elif sent[0] == 'z':
            new_chr = 'a'
        
            
        else:
            
            enc = ord(sent[0]) +1
            new_chr = chr(enc)
        return new_chr + encrypt(sent[1:])
    else:
        return sent[0] + encrypt(sent[1:])
    
#print(sentence)
print('Encrypted message:')
print(encrypt(sentence))        
        