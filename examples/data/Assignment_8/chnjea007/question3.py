# A8Q3

index = 0
newText = ""

def encrypt(s):
    global index
    global newText
    
    currentLetter = s[index]
    
    if currentLetter != " ":
        if currentLetter.islower():
            pos = ord(currentLetter)
            if pos - ord("a") >= 25:
                pos = ord("a") - 1
            pos+=1
            newText+=chr(pos)
        else:
            newText+=currentLetter
    else:
        newText+= " "
    
    index +=1
    if (index<len(s)):
        encrypt(s)
    
    return newText

text = input("Enter a message:\n")
print("Encrypted message:", encrypt(text), sep = "\n") 