def encrypt (userInput):

    if len(userInput) == 0:

        return ''

    if (ord(userInput[0])>= 97) and (ord (userInput[0])<= 122):

        if userInput[0] == 'z':

            return 'a' + encrypt(userInput[1:])

        else:

            return chr(ord(userInput[0])+1) + encrypt(userInput[1:])

    else:

        return userInput[0] + encrypt(userInput[1:])

    

userinput = input ("Enter a message:\n")

print ("Encrypted message:")

print(encrypt(userinput))
