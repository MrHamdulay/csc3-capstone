"""a program to encrypt a message
Yondela Nkwali
06 May 2014"""

#function to encrypt the message
def encrypt (word):
    pos = ord(word[0])
    if word[0] == "":
        return ""
    if word == word.upper():
        return word
    if word[0] == ".":
        return "."
    if word[-1] == "z":
        return encrypt(word[:-1]) + "a"
    if word[0] == " ":
        return  " " + encrypt (word[1:])
    if len(word) == 1:
        return chr(pos+1)
    elif 97<=pos<122:
        return chr(pos+1) + encrypt (word[1:])
    if word[0] == "z":
        return "a" + encrypt (word[1:])
    
#ask for input and output results    
word=input("Enter a message:\n")
result=encrypt(word)
print("Encrypted message:\n",result,sep="")