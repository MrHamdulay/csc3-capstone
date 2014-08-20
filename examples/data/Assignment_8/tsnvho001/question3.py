"""Program to encrypt a message to the next alphabet letter
Tsanwani Vhonani
07 May 2014"""

def msg_encryption(msg):
    first_alphabet="a"
    last_alphabet="z"
    if msg=="":
        return ""
    elif msg[0]== " ":
        return " " +  msg_encryption(msg[1:])
    elif msg[0] != msg[0].lower():
        return msg[0] + msg_encryption(msg[1:])
    elif msg[0]==last_alphabet:
        return first_alphabet + msg_encryption(msg[1:])
    elif msg[0]== '.':
        return '.'
    else:
        letter= ord(msg[0])+1
        return chr(letter) + msg_encryption(msg[1:])
msg=input("Enter a message:\n")
print("Encrypted message:")
print(msg_encryption(msg))