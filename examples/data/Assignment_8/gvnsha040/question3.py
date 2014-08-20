#S.G
word = input("Enter a message:\n")

listZ = []

def encryption(word):
    
    if 97 <= (ord(word[0])) < 122:
        
        x = ord(word[0]) + 1
        listZ.append(chr(x))
        
        if len(word) > 1:
            encryption(word[1:])
            return  ("").join(listZ)
        
        else:
            return ("").join(listZ)
    
    elif (ord(word[0]) == 122):
        x = 97
        listZ.append(chr(x))
        
        if len(word)>1:
            encryption(word[1:])
            return  ("").join(listZ)

        else:
            return ("").join(listZ)        
        
        
    else:

        x = ord(word[0])
        listZ.append(chr(x))
      
        if len(word)>1:
            encryption(word[1:])
            return  ("").join(listZ)

        else:
            return ("").join(listZ)         



coded = encryption(word)

print("Encrypted message:")

print(coded)
