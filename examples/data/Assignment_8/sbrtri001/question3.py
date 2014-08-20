''' Assignment 8, question 3
Recursive function to encrypt a message
Tristan Subroyen
5 May 2014 '''

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
newString = []
def encryptMsg (string):
    ''' This function uses recursion to convert all lowercase characters in a string to its next alphabetical letter '''
    # base case
    if string == '':
        return 0
    
    else:
        # 'z' changes to 'a'
        if string[0] == 'z':
            newString.append('a')
            return encryptMsg (string[1:])
        else:
            # find the letter in the string, append its next alphabetical letter to newString
            if string[0] in alphabet:
                position = alphabet.index(string[0]) + 1
                newString.append(alphabet[position])
                return encryptMsg (string[1:])
            else:
                # if the character is not a lowercase letter, just add to newString and continue recursion
                newString.append(string[0])
                return encryptMsg (string[1:])

# Ask user: input and output result
message = input("Enter a message:\n")
encryptMsg (message)
print("Encrypted message:")
print(''.join(newString))