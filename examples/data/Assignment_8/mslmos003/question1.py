#Rorisang Moseli
#May 2014
#Palindrome Program


def Palindrome(string):
    if len(string)==1:
        print("Palindrome!")
    if len(string)==2:
        if string[0]==string[1]:
            print("Palindrome!")
    if len(string)>2:
        if string[0]==string[-1]:
            return Palindrome(string[1:-1])
        if string[0]!=string[-1]:
            print("Not a palindrome!")

        
string = str(input("Enter a string:\n")) #user inputs a string, the function Palindrome is called and it the string is then evaluated

Palindrome(string)