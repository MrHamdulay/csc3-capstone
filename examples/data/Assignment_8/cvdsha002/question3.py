string= input("Enter a message:\n") #prompts user for input

def encrypt(l):
    if l=="":       #detects empty string
        return l
    elif l[0].islower():    #converts to lowercase
        if l[0]=='z':
            return 'a'+ encrypt(l[1:])        #changes z to a 
        else:
            j=ord(l[0])+1                     #changes j into a unicode number and adds 1 to get the next unicode number for the next letter
            return chr(j)+encrypt(l[1:])         #returns next letter unicode character with a recursion of the rest of the string
            
    else:
        return l[0] + encrypt(l[1:])                  #output
print("Encrypted message:\n"+encrypt(string))

    