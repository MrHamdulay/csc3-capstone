"""encrypt message
Michelle Lu
7 May 2014"""

words=input("Enter a message:\n")

def encrypt(words):
    if words=="":
        return 0
    if words.isupper():
        return words
    elif len(words)==1: #last word
        if 97<=ord(words[0])<122 :
            return chr(ord(words[0])+1)
        elif words[0] == "z": #z gets changed to a
            return "a"
        else:
            return words[0] #punctuation doesn't change
    elif 97<=ord(words[0])<122 :
        return chr(ord(words[0])+1)+ encrypt(words[1:])
    elif words[0] == "z": #z gets changed to a
        return "a" + encrypt(words[1:])
    else: #punctutation doesn't get changed
        return words[0]+ encrypt(words[1:])
        

if encrypt(words)!=0:
    print("Encrypted message:\n", encrypt(words), sep="")
        