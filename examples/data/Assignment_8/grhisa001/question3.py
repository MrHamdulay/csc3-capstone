""" Bella Gorham 
encrypter
06/05/14"""


def encrypt(string):
    if string.isupper():
        return string
    
# if empty return nothing    
    if string == "":
        return ""
# skip over spaces and run again on rest
    
    if string[0] == " ":
        return " " + encrypt(string[1:len(string)])
    if string[0] == ".":
            return "." + encrypt(string[1:len(string)])    
    # if z
    if string[0] == 'z':
            return 'a' + encrypt(string[1:len(string)])    
# if no space move ord up one   
    else:
        return chr(ord(string[0])+1)  + encrypt(string[1:len(string)])
def main():
    message = input("Enter a message:\n")
    print("Encrypted message:")
    print(encrypt(message))
main()