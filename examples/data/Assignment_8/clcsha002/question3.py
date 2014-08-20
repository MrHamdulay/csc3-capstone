"""assignemt 8 question 3
shannon clacey 
8 may 2014"""

def encode(string): #creates the program to encode the given string
        
        if len(string) == 1: #checks if the string is only one letter long
                
                if string.islower(): #checks if the sting is in lower case
                        if string == "z": #checks if the letter is z and if so, in its place, it returns an a
                                return "a"
                        else:
                                return chr(1 +ord(string))#returns the character corresponding to one letter later
                
                else: #if not
                        return string #the string it self. i.e. the string is not in lower case
        
        else: #if the length of the string is not equal to 1 
                return encode(string[0]) + encode(string[1:]) #return the first letter, followed by the letters from position 1 onwards
  
user_input = input("Enter a message: \n")   #gets input from user     
print("Encrypted message:", encode(user_input), sep="\n") #print the final output 

