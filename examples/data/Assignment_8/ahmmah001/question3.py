'''Program to encrypt a given message
Mahnoor Ahmed
10 May 2014'''

def encrypt(msg,n):
    print(n,end="")
  
    #carries out following steps on lowercase characters
    #uses characters unicode values to generate the next character by adding 1 to the unicode value
    if len(msg) == 0:
        return("")
    if len(msg) == 1:
        x= ord(msg[0]) + 1
        if chr(x-1) == "z":
            print("a",end="")
        elif chr(x-1) == ".":
            print(chr(x-1),end="")
        elif msg[0].isupper() == True:
            print(msg[0],end="")
            
        else:
            print(chr(x))
            
    #checks whether character is uppercase, if so, it leaves it as is
    elif msg[0].isupper() == True:
        print(msg[0],end="")
        return(encrypt((msg[1:]), n = ""))   
    
    
    #a space is left as is
    #a "z" is converted to an "a"
    #a "." is left as is
    else:
        x= ord(msg[0]) + 1
        if chr(x-1) == " ":
            print(" ",end="")
            return(encrypt((msg[1:]), n = ""))
        elif chr(x-1) == "z":
            print("a",end="")
            return(encrypt((msg[1:]), n = ""))
        else:
            print(chr(x),end="")
            return(encrypt((msg[1:]), n = ""))
    
encrypt(msg=input("Enter a message:\n"),n="Encrypted message:\n")