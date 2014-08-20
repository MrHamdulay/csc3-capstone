"""Checking for palindromic prime numbers
Christopher Sterley
04/05/2014"""

encode=input("Enter a message:\n")

encode=encode.split()

number=len(encode)-1

def encoder(encode,number):
    if number==-1:
        return ""
    elif encode.isupper():
        return encode
    else:
        if encode[number].isalpha():
            if encode[number]!="z":
                return encoder(encode,number-1) + chr(ord(encode[number])+1)
            else:
                return encoder(encode,number-1) + "a"
        else:
            return encoder(encode,number-1) + encode[number]
    
def full_encoder(encode,position):
    if position==len(encode):
        return ""
    else:
        print(encoder(encode[position],len(encode[position])-1)," ",sep="",end="")
        return full_encoder(encode,position+1)


print("Encrypted message:")
full_encoder(encode,0)