#HLNCEC001
#Question3
#Assignment8
#program that uses a recursive function to encrypt a message

l = []
def encrypt(s):
    global l
    if s == s.lower():
        if ord(s[0]) == 122:
            a = 122 - 26
            s =chr(a)+s[1:]
            return encrypt(s)
        
        elif s[0] != ' ' and (s[0] != '.')  and len(s)!=1:
            new_word = chr(ord(str(s[0]))+1)
            l.append(new_word)
            return encrypt(s[1:])  
        
        elif len(s) == 1:
            if s[0] !='.':
                l.append(chr(ord(str(s[0]))+1))
                print('Encrypted message:\n',''.join(l),sep="")
            else:
                l.append(s[0])
                print('Encrypted message:\n',''.join(l),sep="")
            
        else:
            l.append(s[0])
            return encrypt(s[1:])
    else:
        print("Encrypted message:\n",s,sep='')
    
encrypt(s=input('Enter a message:\n'))