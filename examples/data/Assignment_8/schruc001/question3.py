'''Recursive encryption program
Ruchaan Schmidt
May 2014'''

message = input('Enter a message:\n')
cryptolist = []

def enc (message):
    
    encmes = ''.join(cryptolist)
    
    if message == '':
        print ('Encrypted message:')
        print (encmes)
    #elif message == ' ':
     #   print ('Encrypted message:\n')

    else:
# check for lower case and other
        n = ord (message[0])

# not lower = straigt to list, cut string for recursion       
        if n not in range (97,123):
            cryptolist.append (message[0])
            temp = message[1:len(message)]
            enc (temp)
# lower = convert to ord + 1, then into list, cut string for recursion
        else:
#take care of 'z'            
            if message[0]!='z':
                new = ord(message[0])+1
                cryptolist.append(chr(new))
                temp = message[1:len(message)]
                enc(temp)
            else:
                new = 97
                cryptolist.append(chr(new))
                temp = message[1:len(message)]
                enc(temp)


enc (message)