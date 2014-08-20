#Write a program that uses a recursive function to encrypt a message by converting 
#all lowercase characters to the next character (with z transformed to a).
#Sinead Urisohn
#6 May 2014

#get message
message=input("Enter a message:\n")
#create recursive function to encrypt message that receives message as parameter
def encrypt(s):
    #base case when string empty
    if s=="":
        return ""    
    else:
        #check if character is lower case letter
        if s[0].isalpha() and s[0].islower():
            #if letter is z
            if s[0]=='z':
                #return letter 'a' and recurse through rest of String
                return 'a'+encrypt(s[1:])
            else:
                #convert letter to next letter in alphabet and recurse through rest of String
                return chr(ord(s[0])+1)+encrypt(s[1:])
        #else if it not letter
        else:
            #return character and recurse through rest of String
            return s[0] +encrypt(s[1:])
#display results 
print("Encrypted message:\n"+encrypt(message))