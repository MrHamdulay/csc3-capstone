"""program that uses a recursive function to encrypt a message
Tim Hardie
9 May 2014"""

def encrypt (message):
    if len (message) > 0:
        ord_m = ord (message[0])
        if (97 <= ord_m <= 122):
            if ord_m == 122:
                print (chr (97), end='')
            else:
                print (chr (ord_m + 1), end='')
        else:
            print (message[0], end='')
        encrypt (message[1:])

if __name__ == '__main__':
    message = input ("Enter a message:\n")
    print ("Encrypted message:")
    encrypt(message)