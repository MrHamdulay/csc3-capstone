#Done by Guy Green (Top Secret) (Level Alpha)
#It encrypts a message for you 
#Shhh... Don't tell anyone, it's a secret
#Question 3 Assignment 8


def encrypting(s):
    #Base Case
    if s=="":
        return s
    #If it is inbetween lowercase a and 7
    elif (ord(s[0]))>=ord('a') and ord(s[0])<=ord("z"):
        index=ord(s[0])
        index+=1
        if index>ord('z'):
            index-=26
        return chr(index) + encrypting(s[1:]) #Recursion
    else:
        return s[0] + encrypting(s[1:]) #Recursion

SecretMessage=input("Enter a message:\n")

print("Encrypted message:")
print(encrypting(SecretMessage))