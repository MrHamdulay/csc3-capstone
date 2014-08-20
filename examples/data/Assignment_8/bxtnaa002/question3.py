# question3.py
# program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character
# author: bxtnaa002
# May 2014

msg = input("Enter a message:\n")

def encrypt(msg):
    if len(msg) > 0:
        if msg[0] == " ":
            return " " + encrypt(msg[1:])
        elif (ord(msg[0])) == (ord("z")):
            return "a" + encrypt(msg[1:])
        else:
            if 97<= ord(msg[0])<=122:
                encr_msg = chr(ord(msg[0])+1)
                return encr_msg + encrypt(msg[1:])
            else: return msg[0] +encrypt(msg[1:])
    else:
        return ""
print("Encrypted message:")
print(encrypt(msg))