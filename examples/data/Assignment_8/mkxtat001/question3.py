#MKXTAT001 TATO MOAKI
#Assignment 8 question 3
#Program encrypts a string input 

def encrypt(string):
    """function takes the ASCII value of a number,shifts it one then return the new character"""
    if string == "":
        return ""
    elif string[0] == " ":
        return " " + encrypt(string[1:])
    elif string[0] == "z":
        return "a" + encrypt(string[1:])
    elif string[0] == ".":
        return "." + encrypt(string[1:])
    else: 
        return chr(ord(string[0])+1) + encrypt(string[1:])#chr returns the character value of the numeric value of the shifted characterS

def main():
    user_input = input("Enter a message:\n")
    if user_input == "":
        print() 
    elif user_input.isupper():#checks whether input is upper case or not
        print("Encrypted message:")
        print(user_input)
    else:
        print("Encrypted message:")
        print(encrypt(user_input))
    
if __name__ == "__main__":
    main()
    
