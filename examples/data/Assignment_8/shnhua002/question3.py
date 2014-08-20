"""Encryptonator
Charlie Shang
9 May 2014"""

#Input message to be encrypted...
string = input("Enter a message:\n")

i = 0 #counter to keep track of index within the string

newString = [] #list to accumulate encryted charcaters

def encrypt(string):
    global i
    global newString
    
    new_char = ""

    if i < len(string):  #recursion ends once the last charcter is processed.
       
        askii = ord(string[i]) #retrieve ascii index of char
               
        if askii not in range(97,123): #skip character if not lower case
            newString.append(chr(askii))
            i+=1
            return encrypt(string)
        
        #increase 'a' to 'y' by 1 of ord...
        elif askii in range(97,122):
           
            new_chr = chr(askii + 1)
            newString.append(new_chr)
            i+=1
            return encrypt(string)
        
        #encrypt 'z' as 'a'
        elif askii == 122:
            
            newString.append("a") #exception case when char is 'z'...
            i+=1
            return encrypt(string)
    
    else: #Print new string after all characters are encrypted where relevant.
        newString = "".join(newString)
        print("Encrypted message:\n", newString, sep="")
        
if __name__=="__main__":
    encrypt(string)