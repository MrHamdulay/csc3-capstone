lilwayne=""
def encrypt(word):
    global lilwayne
    if (word==''):
        return lilwayne
    elif(ord(word[0])>96 and ord(word[0])<122):#If the letter is inbetween a and z, including a excluding z
        lilwayne=lilwayne+chr(ord(word[0])+1)
        return encrypt(word[1:len(word)])
    elif(ord(word[0])==122):#if its z, change to a
        lilwayne=lilwayne+'a'
        return encrypt(word[1:len(word)])  
    else:
        lilwayne=lilwayne+word[0]
        return encrypt(word[1:len(word)])  
        
x=input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(x))
