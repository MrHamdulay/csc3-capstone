#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 2014 - 05 - 09
#Function       : Encrypts a message
#Title          : Question3
def encrypt(string):
    """Encrypts test so that each letter is the following letter of the alphabet"""
    #replaces exceptions with a value that comes before there expected output
    if string[0] == "z":
        string = string.replace("z", 'a', 1)
    elif int(ord(string[0])) in range(ord('a'), ord('z') + 1):
        string = string.replace(string[0], chr(ord(string[0]) + 1), 1)

    if len(string) == 1:
        return string  # chr(ord(string[0]) + 1)
    #cuts a string so the next value can be tested
    return string[0] + encrypt(string[1:])


test_value = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(test_value))
