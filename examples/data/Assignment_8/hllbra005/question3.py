# Encryption progrma using recursion
# Brandon Hall (HLLBRA005)
# 09/05/2014

def encrypt(text, position, message): 
    
    if (position < len(text)): #Make sure the sentance does not end
       
        if (text[position].isalpha() and ord(text[position]) > 90):
            
           # print (text[position])
            c = ord(text[position])
            if c != 122:
                message += chr(c+1)
             #   print (c)
             #   print (message)
            else:
                message += 'a'
            #    print (c)
            #    print (message)
                
            position += 1  # Incease the position by 1
            
            return encrypt (text, position, message)
    
        else:
            message += text[position]
            position +=1
            
            return encrypt(text, position, message)
        
            
        
    else:
        return message

    
def Main():
    
    text = input("Enter a message:\n") 


    message = encrypt(text, 0, "") 
    
    print ("Encrypted message:")
    print(message)

Main()