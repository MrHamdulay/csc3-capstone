def encrypt(n = input("Enter a message:\n")):
    if n =='':
        return ''
    
    else:
        a = ord(n[0]) +1
        b = chr(a)
        if (ord(n[0]) == 32):
            b = chr(a-1) 
        else:
            if n[0] == 'z':
                b ='a'
            elif n[0] < chr(97):
                b = n[0]
            else:
                b = chr(a)
        
        print (b,end='')
        return encrypt(n[1:])
    

print('Encrypted message:')
print(encrypt())

        