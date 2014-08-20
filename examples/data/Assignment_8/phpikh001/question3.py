#Ikhlaas Pohplonker
#8 May 2014
#a program that encrypts a message by converting all lowercase characters to the next character
def characters(s):#a recursive function to encrypt a message by converting all lowercase characters to the next character
    dictionary={"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a"," ":" "}#dictionary made
    if len(s)==1 and s[0] in dictionary:
        return dictionary[s[0]]#returns a value from the dictionary
    elif len(s)==1 and s[0] not in dictionary:
        return s[0]#returns the character if it is not in the dictionary
    elif s[0] in dictionary:
        return dictionary[s[0]]+characters(s[1:])#returns a value from the dictionary and calls the recursive function
    else:
        return s[0]+characters(s[1:])#returns the character if it is not in the dictionary and calls the recursive function
    
    
s=input("Enter a message:\n")
print("Encrypted message:\n", characters(s),sep="")