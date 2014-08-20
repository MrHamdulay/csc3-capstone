#Gina Horscroft
#Question 3
#convert all lowercase letters to next character (z -> a)

def encrypt(s):
    if len(s) < 1:
        return ""
    else:
        #check if character is in lowercase
        if (s[0].islower()):
            #if character is z, encrypt to equal a
            if (s[0] == "z"):
                return chr(97) + encrypt(s[1:len(s)])
            #if not z, add 1 to unicode value and convert back to letter
            else:
                return chr(ord(s[0])+1) + encrypt(s[1:len(s)])
        else:
            # if not a lowercase letter return the unchanged character
            return s[0] + encrypt(s[1:len(s)])
        
s = input("Enter a message:\n")
print("Encrypted message:\n", encrypt(s), sep = "")