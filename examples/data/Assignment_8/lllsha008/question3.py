#shaylan lalloo
#LLLSHA008
#encrypts message


myin = input('Enter a message:\n')
#reads input

print('Encrypted message:')

def encrypt(x):
    if len(x) == 0:
        return x
    #if no letters, stop encrypting
    else:
        if 97 <= ord(x[0]) <= 122:
            #check if small letter
            if x[0] == 'z':
                #if z, then add a to the output
                return 'a' + encrypt(x[1:])
            else:
                #otherwise move the letter up by 1
                return chr(ord(x[0]) + 1) + encrypt(x[1:])
        else:
            #else return the character as usual
            return x[0] + encrypt(x[1:])

print(encrypt(myin))
#output the answer
