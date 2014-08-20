"""A program to encode a message
by Jeremy Smith SMTJER002
4 May 2014"""

def encode(string):
    """encodes a message by replacing the character by the letter after the character in the alphabet"""
    #stopping point is if there are no more characters in the string
    if len(string) == 0:
        return ''
    #special cases, where spaces, and punctuation marks mustn't be changed, and 'z' must change to 'a'
    elif string[0] == " ":
        return " " + encode(string[1:])
    elif string[0] == 'z':
        return "a" + encode(string[1:])
    elif string[0] == '.':
        return "." + encode(string[1:])
    #changes the current letter to the letter that follows, and recursively calls the rest of the string
    else:
        letter = ord(string[0]) +1
        return chr(letter) + encode(string[1:])
    
message = input("Enter a message:\n")
#checks that the string contains no upper case letter. Prints the original string if it does contain upper case letters.
if message.islower():
    encode_message = encode(message)
    print("Encrypted message:\n", encode_message, sep='')

else:
    print("Encrypted message:\n", message, sep='')
