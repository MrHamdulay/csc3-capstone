"""Rishen Singh
Assignment 8
Question 3"""
conversion=""
def convert(word):
    global conversion
    if (word==''):
        return conversion
    elif(ord(word[0])>96 and ord(word[0])<122): #checks if letter is between a and z
        conversion=conversion+chr(ord(word[0])+1) #changes character to the next character in alphabet
        return convert(word[1:len(word)]) # runs through rest of the message
    elif(ord(word[0])==122): #if letter is z, changes it to a
        conversion=conversion+'a'
        return convert(word[1:len(word)])  
    else:
        conversion=conversion+word[0]
        return convert(word[1:len(word)])  
        
message=input("Enter a message:\n")
print("Encrypted message:")
print(convert(message))