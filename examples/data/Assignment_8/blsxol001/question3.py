""" a program to encryp a message
xola bilose
09/05/2014"""

def encrypt(message):
    if message =='':
        return ''   
    else :
        if message[0].isalpha():
            if message[0].islower():
                if message[0] == 'z':   
                    a = chr(ord('z') - 25)
                    return a +encrypt (message[1::])
                else:   
                    a = chr(ord(message[0])+1)
                    return a+encrypt (message[1::])
            else:
                a = message[0]
                return a + encrypt(message[1::])
        else: 
            a = message[0]
            return a + encrypt(message[1::])
def main():
    message = input("Enter a message:\n")
    print("Encrypted message:")
    print(encrypt(message))
main()