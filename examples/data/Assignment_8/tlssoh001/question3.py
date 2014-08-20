'''Sohail Tulsi
TLSSOH001
code to encrypt message'''

solid=""
x=input("Enter a message:\n")

#make letters iupac and then add 1
def encrypt(word):
    global solid
    if (word==''):
        return solid

    elif(ord(word[0])>96 and ord(word[0])<122):
        solid=solid+chr(ord(word[0])+1)
        return encrypt(word[1:len(word)])

    elif(ord(word[0])==122):
        solid=solid+'a'
        return encrypt(word[1:len(word)])  

    else:
        solid=solid+word[0]
        return encrypt(word[1:len(word)])  

       
print("Encrypted message:")
print(encrypt(x))