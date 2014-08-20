#Shivam Ragoonaden
#RGNSHI002
#Program that uses recursion to convert all lowercase characters of a string to the next character

message = input("Enter a message:\n")
    
def Encrypt(message):
    
    if message == "":  #Base case
        return ""
        
    elif message[0] == " ":  #Return space
        return " " + Encrypt(message[1:])   
    
    elif (ord(message[0]) < 97):  
        return message[0] + Encrypt(message[1:])   #Capital letters
    
    elif message[0] == "z":  #Odd case
        return "a" + Encrypt(message[1:])
    
    elif not message[0].isalpha():  #if its a character that is not a letter
        return message[0] + Encrypt(message[1:])  #Simply return that character and recall the function for the next character
    
    else:
        return chr(ord(message[0])+1) + Encrypt(message[1:])   #Return the next letter, and recall the function after slicing off the first character
    
x = Encrypt(message)  #Call function
print("Encrypted message:\n" + x)