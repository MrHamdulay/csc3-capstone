"""Create encrypted code
Emmanuel Conradie
09 May 2014"""

#enter message
string = input("Enter a message:\n")
    
def Encrypt(string):
    
    #empty string
    if string == "":  
        return ""
   
    #in case of space    
    elif string[0] == " ":  
        return " " + Encrypt(string[1:])   
   
    #assign number to letters
    elif (ord(string[0]) < 97):  
        return string[0] + Encrypt(string[1:])    
   
    #in case of last letter z
    elif string[0] == "z": 
        return "a" + Encrypt(string[1:])
    
    #check if not letters
    elif not string[0].isalpha():
        return string[0] + Encrypt(string[1:])
    #form new message
    else:
        return chr(ord(string[0])+1) + Encrypt(string[1:])

#print encrypted message    
print_string = Encrypt(string)
print("Encrypted message:\n" + print_string)