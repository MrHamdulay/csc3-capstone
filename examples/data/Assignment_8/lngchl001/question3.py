# encrypts a message by moving the ord of a character+=1
# By Chloe Longmore
# 5 May 2014

message=input("Enter a message:\n")

def encrypter(message):
    #base-case if the string is empty
    if message=='':
        return ''
    # if the next character in the string is a space    
    elif (ord(message[:1]))==32:
        #slices out the space
        message=message[1:]
        #returns a space and recurses
        return " " + str(encrypter(message))
    elif (ord(message[:1]))==46:
        #slices out the full stop
        message=message[1:]
        #returns a full stop and recurses
        return "." + str(encrypter(message))
    elif 65<=(ord(message[:1]))<=90:
        return message
    else:
        # get ord number of letter and add 1  
        letter_no=ord(message[:1])+1
        if letter_no>122:
            letter_no=letter_no -26
        #changes unicode into character
        letter=str(chr(letter_no))
        #slices out first character of string
        message=message[1:]
        #returns the changed character and recurses
        return letter + str(encrypter(message))

        
encrypter(message)
print("Encrypted message:\n",encrypter(message), sep='')