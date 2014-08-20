"""Program to perform simple encryption of lower case strings.
Kemeshan Naicker
7 May 2014"""

#Prompt user for a message to encrypt. (Outside of function so that user is not
#prompted with every repitition of the function.)
msg = input("Enter a message:\n")
#"i" is a counter that allows each recursion to analyse a new index of the
#string successive to the last.
i = 0
#Define a list to collect encrypted characters.
new_msg = []

def encrypt(msg):
    global i
    global new_msg
    new_char = ""

    if i < len(msg):  #Design recursion to terminate once the last character in the string is analysed.
        #Convert character being analysed into unicode equivalent.
        uni_chr = ord(msg[i])
        
        #If character is not a lower-case letter, do not encrypt.
        if uni_chr < 97 or uni_chr > 122:
            new_msg.append(chr(uni_chr))
            i+=1
            return encrypt(msg)
        
        #Encrypt all lower case letters from a to y.  
        elif uni_chr in range(97,122):
            new_chr = chr(uni_chr + 1)
            new_msg.append(new_chr)
            i+=1
            return encrypt(msg)
        
        #If character is "z", wrap around to encrypt to "a".
        elif uni_chr == 122:
            new_msg.append("a") #Hard coded since this is an isolated exception to
            #the encryption process.
            i+=1
            return encrypt(msg)
    
    else: #Print encrypted message only after all characters in the string have been analysed.
        new_msg = "".join(new_msg)
        print("Encrypted message:\n", new_msg, sep="")
        
if __name__=="__main__":
    encrypt(msg)