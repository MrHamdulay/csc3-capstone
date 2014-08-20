#Program to encrpyt message
#Ethan Jackson
#9 May 2014

word = input("Enter a message:\n")
def secret(word):
    if len(word) == 1 and word in "abcdefghijklmnopqrstuvwxy":#if one character,then encrypt that letter
        return chr(ord(word[0]) + 1)
    if len(word) ==1 and word in "z":#if the character is "z", then change it to "a"
        return "a"
    if len(word) > 1 and word[0] in "abcdefghijklmnopqrstuvwxy":#if more than one character, then run through the function for each consecutive character and encrypt it
        return chr(ord(word[0]) + 1) + secret(word[1:])
    if len(word) > 1 and word[0] in "z":
        return "a" + secret(word[1:])
    else:
        if len(word) == 1:
            return word
        else:
            return word[0] + secret(word[1:])
print("Encrypted message:\n"+ secret(word))

        
        
        
        
        
        
        