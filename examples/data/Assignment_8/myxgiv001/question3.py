def encode(string):

    encoded = ""
    if string.isupper():
        return string
    
    if string == "":
        encoded = ""
    elif string[0] !=" ":
        if string[0].isalpha():        
            if string[0]=="z":
                temp="a"        
            else:
                temp= chr((ord(string[0])+1))  
        else:
            temp=string[0]
        encoded+= temp
        encoded+= encode(string[1:])
    else:
        encoded+=" "
        encoded+= encode(string[1:])
    return encoded

string=input("Enter a message:\n")
print("Encrypted message:")
print(encode(string))