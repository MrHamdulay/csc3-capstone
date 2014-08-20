# Question 3 Assignment 8
# James Behr
# 2014-05-05

def encode(letter):
    '''Single character, encode. Lower case letters go to next letter. z goes to a'''
    if not letter.islower():
        return letter
    elif letter == 'z':
        return 'a'
    else:
        return chr(ord(letter) + 1)

def encrypt(message):
    if len(message) == 1:
        return encode(message[0])
    # Slice a string, gradually decreasing its length
    return encode(message[0]) + encrypt(message[1:])

def main():
    print('Enter a message:')
    message = input()
    print('Encrypted message:')
    print(encrypt(message))
    
if __name__ == '__main__':
    main()