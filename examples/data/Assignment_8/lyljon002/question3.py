#9 May 2014
#Program to encrypt a message
#LYLJON002

code = ''                   #initialise coded message

def encrypt(text, code):    #encrypt function
    if text == '':
        return code             #return the coded add
    char = text[0]
    if char.islower():              #check if upper case or not
        if char == 'z':  
            text = text[1:]
            code = code + 'a'
            return encrypt(text, code)   #add to output if orignally z     
        elif char == ' ':
            text = text[1:]
            code = code + char
            return encrypt(text, code)  #add to output if out is a space
        else:   
            text = text[1:]
            code = code + chr(ord(char)+1)
            return encrypt(text, code)      #add to output for normal letters
    else:  
        text = text[1:]
        code = code + char
        return encrypt(text,code)  #return if uppercase


text = input("Enter a message:\n")
print("Encrypted message:\n" , encrypt(text, code), sep='') #output results


