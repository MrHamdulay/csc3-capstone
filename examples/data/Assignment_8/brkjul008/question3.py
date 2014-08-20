#encrypt message
#julia breakey 
#6 may 2014

#encrypt all lowercase letters
def encrypt(word):
    if len(word)==1:
        if 122>=ord(word)>=97:
            if word=="z":
                return "a"
            else: return chr(ord(word)+1)
        else:
            return chr(ord(word))
    else: 
        if 122>=ord(word[0])>=97:
            if word[0]=="z":
                return "a" + encrypt(word[1:])
            else: return chr(ord(word[0])+1) + encrypt(word[1:])
        else:
            return chr(ord(word[0])) + encrypt(word[1:])

#as for message
string=input("Enter a message:\n")

#return encryption
print("Encrypted message:\n", encrypt(string), sep="")
