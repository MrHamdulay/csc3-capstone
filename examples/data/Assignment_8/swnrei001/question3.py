"""Question 3 of Assignment 8
Encrypts a message by incrementing the value of each char by one, with z -> a
SWNREI001
05/05/2014"""

def encrypt(msg):
    """Encrypts string msg by incrementing each lowercase character by one in 
    the alphabet, returning the encrypted string"""
    if msg == "": # base case: empty string
        return ""
    else:
        nextchar = msg[0] # variable stores encrypted char
        if msg[0].islower():
            nextchar = chr(ord(msg[0]) + 1) # only encrypt if lowercase
        if msg[0] == 'z':
            nextchar = 'a' # wraparound; z becomes a
        return nextchar + encrypt(msg[1:]) 
    
def main():
    """Main function of module - gets input from user and outputs the encrypted
    version of the input"""
    msg = input("Enter a message:\n")
    print("Encrypted message:")
    print(encrypt(msg))
    
if __name__ == "__main__":
    main()