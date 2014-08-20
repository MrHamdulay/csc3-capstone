"""program to encrypt a message by converting all lowercase characters to the next character (with z transformed to a)
Muhammad Nabeel Dulymamode
08/05/2014"""
Ord_A = 65
Ord_a = 97
Ord_0 = 48
n_alpha = 26
n_digit = 10

def encrypt(message, step):
    #encrypt a message by converting all alphanumeric characters to the character n steps after it
    if len(message) > 0:
        Ord_no = ord(message[0])
        if Ord_no >= Ord_A and Ord_no < Ord_A + n_alpha:
            Ord_no -= Ord_A
            return chr(Ord_A + (Ord_no + step)%n_alpha) + encrypt(message[1:],step)
        elif Ord_no >= Ord_a and Ord_no < Ord_a + n_alpha:
            Ord_no -= Ord_a
            return chr(Ord_a + (Ord_no + step)%n_alpha) + encrypt(message[1:],step)
        elif Ord_no >= Ord_0 and Ord_no < Ord_0 + n_digit:
            Ord_no -= Ord_0
            return chr(Ord_0 + (Ord_no + step)%n_digit) + encrypt(message[1:],step)
        else:
            return message[0] + encrypt(message[1:],step)
    else:
        return ""

def encryptalpha(message, step):
    #encrypt a message by converting all lowercase characters to the character n steps after it
    if len(message) > 0:
        Ord_no = ord(message[0])
        if Ord_no >= Ord_a and Ord_no < Ord_a + n_alpha:
            Ord_no -= Ord_a
            return chr(Ord_a + (Ord_no + step)%n_alpha) + encryptalpha(message[1:],step)
        else:
            return message[0] + encryptalpha(message[1:],step)
    else:
        return ""

def decrypt(message, step):
    #decrypt a message by converting all alphanumeric characters to the character n steps befre it
    if len(message) > 0:
        Ord_no = ord(message[0])
        if Ord_no >= Ord_A and Ord_no < Ord_A + n_alpha:
            Ord_no -= Ord_A
            return chr(Ord_A + (Ord_no - step)%n_alpha) + decrypt(message[1:],step)
        elif Ord_no >= Ord_a and Ord_no < Ord_a + n_alpha:
            Ord_no -= Ord_a
            return chr(Ord_a + (Ord_no - step)%n_alpha) + decrypt(message[1:],step)
        elif Ord_no >= Ord_0 and Ord_no < Ord_0 + n_digit:
            Ord_no -= Ord_0
            return chr(Ord_0 + (Ord_no - step)%n_digit) + decrypt(message[1:],step)
        else:
            return message[0] + decrypt(message[1:],step)
    else:
        return ""

#test_cases = {"Hello world!":1, "Hello world0!":10, "Hello world12!":27, "Hello World007!":1}
def test(test_cases):
    for msg in test_cases:
        if decrypt(encrypt(msg, test_cases[msg]), test_cases[msg]) == msg:
            print(True)
        else:
            print(False)

#test(test_cases)

msg = input("Enter a message:\n")
enc_msg = encryptalpha(msg,1)
print("Encrypted message:",enc_msg, sep = "\n")