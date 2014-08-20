#Kovlin Perumal
#PRMKOV001
#09/05/2014
#Encrytption Function

inputPhrase = input("Enter a message:\n")

def encrypt(dummy) :
    
    if len(dummy) > 0 :
        if dummy[0] == 'z' :#Account for z changing to a
            return 'a' + encrypt(dummy[1:])
        elif dummy[0].isalpha() :
            if dummy[0].islower():#Check if lower letter
                return chr(ord(dummy[0]) + 1).lower() + encrypt(dummy[1:])#Convert to unicode to change letter one forwards
            else:
                return dummy[0] + encrypt(dummy[1:]) #Else return original character
        else :
            return dummy[0] + encrypt(dummy[1:])
    else :
        return ''

print("Encrypted message:\n" + encrypt(inputPhrase))
