"""program to encrypt a message
author: DIVAN JAGERS
date: 9 May 2014"""
def Encrpt(string):
    if string =='':    #base case
        return ''
    
    else:
        encrptd = chr(ord(string[0]) +1)  #shifts each character one unit up
        if string[0] == 32:     #checks if the character was an " "
            encrptd = chr(ord(encrptd)-1)    #if it was an " " then it will not shift this character but rather retain it
        else:
            if string[0] == 'z': #if the character is a "z" , it will become an a
                encrptd ='a'
            elif string[0] < chr(97):   #checks if it is a capital letter
                encrptd = string[0]
            else:
                encrptd = chr(ord(string[0])+1)   #finally shifts all characters
        
        print (encrptd,end='')     # prints the encrptd message
        return Encrpt(string[1:]) #the iteration step
    
string= input("Enter a message:\n")  #prompts the user for input

print('Encrypted message:')
print(Encrpt(string))