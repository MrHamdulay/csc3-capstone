#Kiuran Naidoo
#Assignment 8
#Question 3
#5 May

def encrypt(word, num =0):#Function to encrypt
    if num < len(word):
        if word[num].islower():#Check character is lower case
            if word[num] != 'z':
                word = word[:num]+chr(ord(word[num])+1)+word[num+1:]#next lower case character replacement
            else: #Special case for 'z'
                word = word[:num]+'a'+word[num+1:]
        return encrypt(word,num+1)
    return word

inputMessage = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(inputMessage))
    
