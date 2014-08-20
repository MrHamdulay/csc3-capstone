#Program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character
#Saul Bloch
#7 April 2014

user_string = input ("Enter a message:\n")

def encrypt_message (user_sentence):
    length_of_message = len(user_sentence)
    if length_of_message == 0:
        return ''
    elif (ord(user_sentence[0])>= 97) and (ord(user_sentence[0])<= 122):
        if user_sentence[0] == 'z':
            return 'a' + encrypt_message(user_sentence[1:])
        else:
            return chr(ord(user_sentence[0])+1) + encrypt_message(user_sentence[1:])
    else:
        return user_sentence[0] + encrypt_message(user_sentence[1:])
   

print ("Encrypted message:")
print(encrypt_message(user_string))