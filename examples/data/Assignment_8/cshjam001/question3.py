"""Creating secret code using unicode
James Cushway
10-05-2014"""
position=0
word=input('Enter a message:\n')
print('Encrypted message:')
def secret_code(position):
    if position<len(word):
        if word[position]!=' ' and word[position].islower() and word[position]!='z':
            number=chr(ord(word[position])+1)
            print(number,end='')
            position+=1
            secret_code(position)
        elif word[position]=='z':
            print(chr(ord('z')-25),end='')
            position+=1
            secret_code(position)
        else:
            number=chr(ord(word[position]))
            print(number,end='')
            position+=1
            secret_code(position)            

            
        
        
        
secret_code(position)