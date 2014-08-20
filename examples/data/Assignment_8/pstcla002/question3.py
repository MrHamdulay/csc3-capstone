""""Finding palindrome primes between two inputs
Claudia Pastellides
8 May 2014"""

def encrypt(word):
    if len(word) == 1:
        if word.islower(): #checks if word is lower case
            if word == 'z':
                return 'a'
            else:
                return chr(ord(word) + 1) #creates encrypted word
        else:
            return word
    else:
        return encrypt(word[0]) + encrypt(word[1:])

string = input("Enter a message:\n") #gets user input
print("Encrypted message:")
print(encrypt(string)) #prints output
