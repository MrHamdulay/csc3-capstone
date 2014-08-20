def encode(sentence):
    if len(sentence)==1:
        firstletter=sentence[0]
        char=ord(firstletter)
        if firstletter=="z":
            newchar="a"       
        elif firstletter.islower():
            newchar=chr(char+1)
        else:
            newchar=firstletter
        return newchar
    else:
        firstletter=sentence[0]
        char=ord(firstletter)
        if firstletter=="z":
            newchar="a"
        elif firstletter.islower():
            newchar=chr(char+1)
        else:
            newchar=firstletter
        newsentence=sentence[1:]
        return (newchar + encode(newsentence))
    

sentence=input("Enter a message:\n")

print("Encrypted message:\n", encode(sentence), sep="")