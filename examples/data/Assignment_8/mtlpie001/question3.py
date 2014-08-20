#PIET MOTALAOTA
#11 MAY 2014
def message(word):
    if len(word)<1:
        return ""
    if word[0].isalpha() and word[0].islower():
        if word[0]=="z":
            return chr(97) + str(message(word[1:]))
        else:
            return chr(ord(word[0])+1) + str(message(word[1:]))
    else :
        return word[0] + str(message(word[1:]))
    
if __name__=="__main__":
    word=input("Enter a message:\n")
    print("Encrypted message:\n"+message(word))
    