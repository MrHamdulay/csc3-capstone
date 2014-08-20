""" Encrypt message by changing lower case letters to the next letter
Roger Cox
8 may 2014 """

def code (string,new_word):

    x=(ord(string[0])) # convert into unicode
    
    
    if len(string)> 1  : # base case
        if 97<=x<= 121 : # normal alphabet
            x+=1
            y=chr(x)
            new_word += y 
            return (code(string[1:],new_word))
            
        elif  x==122 : # for z
            y=chr(x-25)
            return (code(string[1:],new_word+y))
        
        else : # for any other charactor
            #new_word += string[0]
            return (code(string[1:],new_word+string[0]))
    else: 
        if 97<=x<= 121 : # for last letter
            x+=1
            y=chr(x)
            new_word += y 
            return new_word
               
        elif  x==122 :
            y=chr(x-25)
            return (new_word+y)
           
        else :
            
            return (new_word+string[0])      
     
  
string=(input("Enter a message:\n"))  
print("Encrypted message:")
print(code(string,""))



