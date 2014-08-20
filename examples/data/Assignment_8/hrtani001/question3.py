#Aniq Hartle
#09/05/2014
#shift all lowercase letters one character up 1

'''shifts all lowercase characters in the input string one character up 1'''
def encrypt(userI):
    if userI[0]==" ":
        return " "+encrypt(userI[1:])
    elif userI[0]==userI[len(userI)-1]:        #if the last remaining letter is lowercase change otherwise leave it
        if userI[0].islower():
            if userI[0]=="z":                       #if the first character is in lowercase and is z, -
                return "a" 
            else:
                return chr(ord(userI[0])+1)
        else:
            return userI[0]
    elif userI[0].islower():
        if userI[0]=="z":                       #if the first character is in lowercase and is z, -
            return "a"+encrypt(userI[1:])       #-set it to a, otherwise increace it 1 character
        else:            
            return chr(ord(userI[0])+1)+encrypt(userI[1:])
    elif userI[0].isupper():
        return userI[0]+encrypt(userI[1:])      #if the character is in upper case, make no changes and continue
    else:
        return encrypt(userI[1:])

#take user unput and apply encryption, output result    
userInput = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(userInput))