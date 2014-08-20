#Program that encrypts a sentence
#Gordon Skhosana
#8/05/2014

def encrypt(message):
    if message=="":
        return ""
    elif message[0]=="z":
        return "a" + encrypt(message[1:len(message)])
    elif message[0]==" ":
        return " " + encrypt(message[1:len(message)])
    elif message[0]==".":
        return "." + encrypt(message[1:len(message)])
    else:
        code=ord(message[0])+1
        charact=chr(code)
        return (charact) + encrypt(message[1:len(message)])
def main():
    message=input("Enter a message:\n")
    LcaseMessage=message.lower()
    if message=="":
        print("")
    elif (ord(LcaseMessage[0]))==ord(message[0]):
        print("Encrypted message:\n",encrypt(message),sep="")
    else: 
        print("Encrypted message:\n",message,sep="")
main()
