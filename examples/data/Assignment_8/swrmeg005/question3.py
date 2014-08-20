#Program to move characters one down
#By Megan Swartz
#12th May 2014

#moves all lowercase letter in string one character down
def letterchange(string):
    if string=='':
        return ''
    letter=string[0]
    if 97<=ord(letter)<=122:    #Checks if letter being evaluated is between a and z
        if letter=="z":
            return "a"+letterchange(string[1:])
        else:
            return chr(ord(letter)+1)+letterchange(string[1:])
    else:
        return letter+letterchange(string[1:])

#Asks for input and returns changed string
string=input("Enter a message:\n")
print("Encrypted message:\n",letterchange(string),sep='')