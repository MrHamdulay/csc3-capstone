#Saijil Nemchund
#NMCSAI001
#Question 3

x=input("Enter a message:\n")
print("Encrypted message:")

yeah=""
def encrypt(word): 
    global yeah
    if (word==''):  #checking to see if the input is an empty string 
        return yeah
    elif(ord(word[0])>96 and ord(word[0])<122):  #if it's not an empty string
        yeah=yeah+chr(ord(word[0])+1)     #changes each letter to the next letter in the alphabet after it 
        return encrypt(word[1:len(word)])
    elif(ord(word[0])==122):
        yeah=yeah+'a'
        return encrypt(word[1:len(word)])  #changes the "z" to an "a"
    else:
        yeah=yeah+word[0]
        return encrypt(word[1:len(word)])  #displays a number when  a number is entered as ouput 

print(encrypt(x))