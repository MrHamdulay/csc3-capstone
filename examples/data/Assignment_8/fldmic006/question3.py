#code to take a message and change each character in the message to the next character
#michael field
#5 may 2014

#MUST NOT CHANGE UPPERCASE THEREFORE CHECK IF THE CHARACTER IS LOWER OR UPPERCASE
def coder(message, count, new):
    char = ''
    
    
    
    if message == "":
        return ""
    
    elif count < len(message):
        char = message[count]
        lowChar = char.lower()   
        
        #check if each character is lowercase
        if char == lowChar:        
            #change z
            if (ord(char) == 122):
                char = 'a'
                count += 1
                new += char + coder(message, count, new)
             
            #space  
            elif (ord(char) == 32):
                count += 1
                new += char + coder(message, count, new) 
            
            #full stop
            elif (ord(char) == 46):
                count += 1
                new += char + coder(message, count, new)
                
            #change rest
            else:
                num = ord(char)
                num += 1
                char = chr(num)
                count += 1
                new += char + coder(message, count, new)
                

                #for the uppercase letters
        else:
            count += 1
            new += char + coder(message, count, new)
            
        return new
    
    else:
        return new
message = input("Enter a message:\n")
count = 0
new = ""

coded = coder(message, count, new)
print("Encrypted message:")
print(coded)
