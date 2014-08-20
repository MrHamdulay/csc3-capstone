#Question 3
#Tase Ngambi
#6 May 2014

def encrypt(message):
    if not message:
        return ""
    
    else:
        if message[0] != " ":
            
            val = message[0]
            if message[0].islower():
                empt = ord(message[0])+1
                val = chr(empt)
                
            #case where letter is z
            if message[0] == 'z':
                val = chr(97)
            #checking its lower case    
            
            return val + encrypt(message[1:])
          
        else:
            return " "+encrypt(message[1:])
        
print("Enter a message:")
message = input()
print("Encrypted message:")
print(encrypt(message))
          
          