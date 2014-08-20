# Author : Rayaan Fakier FKRRAY001
# Date : 08 - 05 - 2014
# question3.py

def encrypt(string, new_string):
    '''Recursive function that encrypts a message'''
    # Base case - Once the string has been completely run through
    if len(string) == 0:
        return print("Encrypted message:\n" + new_string)
    # Recursive step - converts string into encoded characters
    elif string.islower():
        num = ord(string[0])
        if num == 122:
            num = 97
        elif (num < 97) or (num > 122):
            num = num
        else:
            num += 1
        
        new_string += chr(num)
        return encrypt(string[1:],new_string)
    else:
        new_string += string[0]
        return encrypt(string[1:],new_string)
if __name__ == '__main__':
    new_string = ""
    string = input("Enter a message:\n")
    encrypt(string, new_string)