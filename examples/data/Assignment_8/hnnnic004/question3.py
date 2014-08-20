'''program to encrypt a message using recursion
nicole henning
due 9 may 2014'''

message = input("Enter a message:\n")
list_message = []

def encrypt(message):
    
    if len(message) == 1: #ie last charcter of string
        if message.isalpha() == True: #if a letter and lower case
            if message.islower() == True:
                    
                    if message == "z":
                        list_message.append("a") #z changes to a, add to existing list           
                    else:
                        encoded = chr(ord(message)+1) #any other lowercase letter gets changed to the following letter of the alphabet 
                        list_message.append(encoded) #add to existing list
            #anything that is not a letter/is capitalised stays the same
            else: 
                list_message.append(message)            
        else:
            list_message.append(message)
       
       
    elif len(message)>=2: #ie for string with more than one character, not at end yet  
        if message[0].isalpha() == True: #if a letter and lower case
            if message[0].islower() == True:
        
                    if message[0] == "z":
                        list_message.append("a") #z changes to a, add to existing list 
                        return encrypt(message[1:]) #encrypt the rest of the letters in the string
                               
                    else:
                        encoded = chr(ord(message[0])+1) #any other lowercase letter gets changed to the following letter of the alphabet 
                        list_message.append(encoded) #add to existing list
                        return encrypt(message[1:])
            #anything that is not a letter/is capitalised stays the same
            else:
                list_message.append(message[0])
                return encrypt(message[1:])            
        else:
            list_message.append(message[0])
            return encrypt(message[1:]) 
                                   
            
        return list_message #return entire encrypted list
    encoded_message = "".join(list_message) #change encrypted list into encrypted string
    print("Encrypted message:",encoded_message, sep="\n") #displays encrypted message


encrypt(message)
