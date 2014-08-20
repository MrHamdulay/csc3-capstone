'''program to encrypt message using ASCII values - convert everything to lower case and to the next letter
Thabiso Beau
4 May 2014
Assignment 8: question3.py'''

x = input('Enter a message: \n')
message= ''
def encrypt(x):
    global message
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if x[:]=='': #setting base case for program - if empty string
        return message
    else:
        if x[0] == 'z': #if there's a z - convert to a
            message +='a'
            return encrypt(x[1:])
        
#else condition// use ord function and add 1 - thereafter use chr function to convert back to the letter
        elif x[0] in alpha:
            message += chr(ord(x[0])+1)  # + encrypt(x[1:])
            return encrypt(x[1:])
        #elif x[0] == ' ':
         #           message +=" "
          #          return encrypt(x[1:])
        else:
            message += x[0]
            return encrypt(x[1:])
    
    
y = encrypt(x)
print('Encrypted message:\n', y, sep='')
