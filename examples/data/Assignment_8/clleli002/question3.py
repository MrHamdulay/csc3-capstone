"""Encrypt a message using recursive function
Elizabeth Cilliers
14/05/05"""

def code(string):
    
    
            if len(string)==0:
                        return ""
            
            if len(string)>0:
                    
                        if (string[0])==" ": #check for spaces
                                    string=string[1:]
                                    return " "+code (string)
                        
                        elif (ord(string[0]))==122: #check for letter z
                                    new_string= "a"
                                    string=string[1:] #slice of character in string
                                    return new_string + code(string) 
                                                                                
                                                    
                        elif 46<=(ord(string[0]))<=90: #check for capital letter and punctuation
                                    new_string=string[0]
                                    string=string[1:]
                                    return new_string + code(string)                                          
                    
                        else:
                                    new_string=chr(ord(string[0])+1) #change character to following character in alphabet 
                                    string=string[1:]
                                    return new_string + code (string)    
                                
                                        
string=input("Enter a message:\n")
print("Encrypted message:")
print(code(string))