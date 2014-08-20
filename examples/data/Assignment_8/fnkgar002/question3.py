"""Program to encrypt a message 
Gary Finkelstein
6 May 2014"""


def encrypt_word (sentence):
    if len(sentence) == 0:     #if no word, dont encrpyt, just return blank string
        return ""
    #find the ascii value for each letter and if the letter is z, then it must be encrypted to 'a'
    if (ord(sentence[0])>= 97) and (ord (sentence[0])<= 122):
        if sentence[0] == "z":
            return "a" + encrypt_word(sentence[1:])
        #if the ascii value for each letter and move the number up by 1, then convert back to character and recall the function
        else:
            return chr(ord(sentence[0])+1) + encrypt_word(sentence[1:])
    else:
        return sentence[0] + encrypt_word(sentence[1:])


#allows user to enter message  
user_input = input ("Enter a message: \n")
#displays encrypted word after calling the encrypt word method
print ("Encrypted message:")
print(encrypt_word(user_input))