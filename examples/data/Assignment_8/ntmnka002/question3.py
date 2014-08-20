def encrypt(s, k):
    
    new = ''
    if len(s) == 0:
        return k
    else:
        if s[0].islower():
            
            if s[0] == 'z':
                new = 'a'
                k += new
                return encrypt(s[1:], k)
            
            else:
        
                new = chr(ord(s[0]) + 1)
                
                k += new
                
                return encrypt(s[1:], k)
        else:
            k += s[0]
            return encrypt(s[1:], k)
        
k = ''   
word = input('Enter a message:\n')
out = encrypt(word, k)
print('Encrypted message:')
print(out)