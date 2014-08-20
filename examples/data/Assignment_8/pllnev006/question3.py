#Program to encrypt message
#Nevarr Pillay - PLLNEV006
#4 May 2014

def encrypt(message):
    """Encrypts a message by changing all lowercase values"""
    if message == "": # Stops if message is empty
        return ""
    else:
        char = message[0] # First letter of string
        if char.islower(): # Checks to see if its in lower case
            if char == "z": # Makes it a if z
                newchar = chr(ord(char) - 25)
            else: # Othewises uses the character after it in Unicode
                newchar = chr(ord(char) + 1)
            return newchar + encrypt(message[1:])
        else:
            return char + encrypt(message[1:])
        
def main():
    message = input("Enter a message:\n")
    print("Encrypted message:",encrypt(message),sep="\n")
        
if __name__ == "__main__":    
    main()
            