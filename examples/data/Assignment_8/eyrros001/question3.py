"""recursive function to encrypt a message by converting all lowercase characters to the next character
Ross Eyre
05/05/2014"""

def main():
    msg = input("Enter a message:\n")
    print("Encrypted message:\n" + str(encrypt(msg)))

xhar = ''
    
def encrypt(string):
    
    global xhar 
    
    if(len(string)==0): #if string contains nothing, we are done
            return xhar
        
    elif(ord(string[0:1:]) > 96 and ord(string[0:1:]) < 122): #if current char is alpha and not z
        
        newUni = ord(string[0:1:]) + 1 #make next character in alphabet
        xhar += chr(newUni)
        return encrypt(string[1::]) #call function again 
         
    elif(string[0:1:]=='z'):
        xhar += 'a' # else 'z' must become 'a'
        return encrypt(string[1::])        
        
    else:
        xhar += (string[0:1:])
        return encrypt(string[1::])      
    
main()