#Darryl Gounden
#Enrypts a string to the next letter for each letter in the string

word = input("Enter a message:\n")
listing = []

def encrypt(word):
    
    if 97 <= ord(word[0]) < 122:
        x = ord(word[0]) + 1
        listing.append(chr(x))
        if len(word)>1:
            encrypt(word[1:])
            return  ("").join(listing)
        else:
            return ("").join(listing)
    
    elif (ord(word[0]) == 122):
        x = 97
        listing.append(chr(x))
        #encrypt(word[1:])
        if len(word)>1:
            encrypt(word[1:])
            return  ("").join(listing)
        else:
            return ("").join(listing)        
        
        
    else:
        x = ord(word[0])
        listing.append(chr(x))
        #return encrypt(word[1:])
        if len(word)>1:
            encrypt(word[1:])
            return  ("").join(listing)
        else:
            return ("").join(listing)         

encrypted = encrypt(word)

print("Encrypted message:")
print(encrypted) 

    

