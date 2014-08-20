#program to move the letters in a string one up in the alphabet
#kiyarah pillay
#10 may 2014

#get input from user
message=input("Enter a message:\n")
#create empty string
string=""
def alphabet(message):
    global string
    if message=="":
        return string
#checking if the letters are lowercase
    elif 122>ord(message[0])>96 :
        string+= chr(ord(message[0])+1)
        return alphabet(message[1:])
    elif message[0]=='z':
        string+='a'
        return alphabet(message[1:])
    else:
        string+=message[0]
        return alphabet(message[1:])
        
print ("Encrypted message:\n" ,alphabet(message), sep="")
    
