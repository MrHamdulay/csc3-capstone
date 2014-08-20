"""encrypter
Joshua Hewitson
2/5/2014"""

global string2
string2 = ""

def encrypt(input1):
    # input1 is shortened each time and if it is of length 0 the whole message has been encrypted
    if len(input1) == 0:
        return
    
    # if the starting letter is z an a is added to the output string:
    if input1[0] == 'z':
        global string2
        string2 += 'a'
        #the first letter of input1 is removed and encrypt is run again
        input1 = input1[1:len(input1)]
        encrypt(input1)
        
    elif input1[0].islower():
        # if the first letter is lowercase and not a z then the next character in the alphabet is added to the output string
        string2 += chr(ord(input1[0]) + 1)
        #the first letter of input1 is removed and encrypt is run again
        input1 = input1[1:len(input1)]
        encrypt(input1)        
    else:
        #if the first letter is uppercase, then the letter is added unchanged to the output string
        string2 += input1[0]
        #the first letter of input1 is removed and encrypt is run again
        input1 = input1[1:len(input1)]
        encrypt(input1)          

string1 = input("Enter a message:\n")
encrypt(string1)
print ("Encrypted message:\n" , string2, sep = "")