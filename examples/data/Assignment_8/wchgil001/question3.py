#Write a program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a)
#Gillian Wachira
#09 May 2014

def base(message):
#base case for empty string
    if message == "":
        return ""
    
#base case for capital letter message
    elif message == message.upper():
        return message
    
 #"extra" base cases due to the fact that we are using ord and chr.
    elif message[0] == " ":
        return " " + base(message[1:])
    elif message[0] == "z":
        return "a" + base(message[1:])
    elif message[0] == ".":
        return "." + base(message[1:])
    
  #"main" recursive function
    else:
        return chr(ord(message[0])+1) + base(message[1:])
    

def main():
    y = input("Enter a message: \n")
    print("Encrypted message:")
    print(base(y))
    print()
    
       
main()