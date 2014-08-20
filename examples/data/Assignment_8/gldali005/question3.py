#program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character 
#Ali Goldstein
#8 May 2014

def encryptmessage(message,length):
    if length==-1:
        #This will stop the recursion as the entire term has be converted
        print('',end='')
    else:
        original=ord(message[length])
        #This is finding the ASCII values of the character entered in by the user
        if (original ==32):
            original = original 
        elif (original ==122):
            #This is checking if the letter is a 'z', as 'z' is changed to 'a'
            original = 97
        elif (original>=97 and original<122):
            original= original+1            
        else:
            original=original
        new=chr(original)
        tot = encryptmessage(message,length-1)
        print(new,sep='',end='')

#prompt the user to enter a message 
message = input("Enter a message:\n")
message.lower()
#call the function to encrypt the message
print("Encrypted message:")
length = len(message)
(encryptmessage(message,length-1))
