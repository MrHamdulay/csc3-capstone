def encode(x):
    if not x:
        return 0
    else:
        if x[0].islower():
            
            if x[0]!= 'z':
                print (chr(ord(x[0])+1), end = "")
            else:
                print('a', end = "")
        else:
            print(x[0], end = "")
        return encode(x[1:])
        
    
    


message = input("Enter a message:\n")
print('Encrypted message:')
(encode(message))
