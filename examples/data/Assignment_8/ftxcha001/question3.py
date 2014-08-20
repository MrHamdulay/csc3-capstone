#Chantel Foot
#Question 3 
#Assignment 8

string = input("Enter a message:\n")

def encrypt(word):
    if len(word) == 1: #only 1 letter in the string
        
        if word[0].islower(): #if first letter in lower case 
            
            if word[0] == "z": # base case 
                return "a" #if that letter is z then change to a 
            
            else:
                return chr(ord(word[0])+1) #giving letter a value, adding 1 to that value and then getting corresponding value to new letter 
        else:
            return word
        
    else:
        return encrypt(word[0]) + encrypt(word[1:])                 
                
                       
print("Encrypted message: ")
print(encrypt(string))



                
                    
            
            