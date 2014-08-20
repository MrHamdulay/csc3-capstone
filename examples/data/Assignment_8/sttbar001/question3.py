"""encrypt a message by converting all lowercase characters to the next character (with z transformed to a)
barak setton
04/05/2014"""

def enc(s):
    if len(s)==1:    # telling it when to stop
        num = ord(s)
        if s[0].isupper() or s[0] ==" " or ord(s[0])<97 or ord(s[0])>122: # checking that the charater is not in uppercase, is a space or is not in the alphabet
            return s[0]
        elif s=="z":    # is z take it to a and not {
            return "a"
        else:
            return chr(num+1) # return the last charature in the string
    else:
        if s[0].isupper() or s[0] ==" ":       # checking if character in uppercase
            return s[0]+enc(s[1:]) # return with the uppercase remaining
        
        elif s[0]=="z":
                return "a"+enc(s[1:])        
        else:
            return chr(ord(s[0])+1)+enc(s[1:])   # return the new charater with the rest of string

s =input("Enter a message: \n")
encode = enc(s)
print("Encrypted message: ")
print(encode)
