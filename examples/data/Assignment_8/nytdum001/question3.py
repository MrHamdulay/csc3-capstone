"""Program to to encrypt a message
Dumisani J Nyathi
09-05-2014"""

def encode(string):
    encoded = ""
    if string.isupper():
        return string
    elif string == "":
        encoded = ""
    elif string[0] !=" ":
        if string[0].isalpha():        
            if string[0]=="z":
                x="a"  #to account for last letter      
            else:
                x= chr((ord(string[0])+1))  
        else:
            x=string[0]
        encoded+= x
        encoded+= encode(string[1:])
    else:
        encoded+=" "
        encoded+= encode(string[1:])
    return encoded

def main():
    string=input("Enter a message:\n")
    print("Encrypted message:")
    print(encode(string))#calls recursive function
    
main()