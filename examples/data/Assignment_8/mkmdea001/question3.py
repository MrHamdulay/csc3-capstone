#dean makambwa
#6/05/14
#prog to encrypt a message 

#get input from user 
x=input('Enter a message:\n')


def encrypt(x):
    #check if input is empty or a space and if it is return either a space or nothing 
    if x=='':
        return''
    elif x==' ':
        return' ' + encrypt(x[1:])
    #if the first letter is a z then change it to a and then slice the first letter off and continue with the message 
    elif x[0]=='z':
        return 'a'+ encrypt(x[1:])
    #if it is part of the alphabet, then return as is and continue with the message 
    elif x[0] is x.isalpha:
        return x[0] + encrypt(x[1:]) 
    #if it is a capital then return as is and continue with the slicing
    elif (ord(x[0])<97):
        return x[0] + encrypt(x[1:])
    #otherwise after checking the order of the letter add one then return the character of that order then continue sliceing 
    else:
        return chr(ord(x[0])+1)+encrypt(x[1:])
#create a variable of the function then use it to print the characters returned
m=encrypt(x)

print('Encrypted message:\n'+m)

