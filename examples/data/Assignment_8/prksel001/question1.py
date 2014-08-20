'''Checking if word is a palindrome
09/05/2014
Limpho Parkies'''

string=input("Enter a string:\n")

def palin(string):
    if len(string)==1 or len(string)==0:
        print('Palindrome!')
    else:
        if string[0]==string[len(string)-1]:
            return palin(string[1:len(string)-1])
        else:
            print('Not a palindrome!')
palin(string)