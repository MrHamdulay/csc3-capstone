"""Assignment 8, Question 3
Tejasvin Bagirathi BGRTEJ001
program to encrypt string"""

string = input('Enter a message:\n')
pos = 0
en_string = []
def encrypt(string):
    global pos
    global en_string
    new_asc = ''
    
    #Terminates recursive function on final character
    if pos < len(string):
        asc_chr = ord(string[pos])
    
        #Prevents any characrter which is nto lowercase from being encrypt
        if asc_chr < 97 or asc_chr > 122:
            en_string.append(chr(asc_chr))
            pos += 1
            encrypt(string)
        #Encrypt all lower case letters, except z
        elif asc_chr in range(97, 122):
            new_asc2 = chr(asc_chr + 1)
            en_string.append(new_asc2)
            pos += 1
            return encrypt(string)
        #Special case if character is z
        elif asc_chr == 122:
            en_string.append('a')
            pos += 1
            return encrypt(string)        
        
    #Join the string together and print out the encrypted message
    else:
        en_string = ''.join(en_string)
        print('Encrypted message:\n', en_string, sep = '')
        
if __name__=="__main__":
    encrypt(string)