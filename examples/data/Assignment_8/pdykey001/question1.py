"""Palindrome using recursion
Keyoolin Padayachee
9 May 2014"""

string = input("Enter a string:\n")
string2 = " " #initialising the reverse string

def reverse(string,string2):
    length=len(string)     
    if length != 0:
        letter = string[-1] #gets the last letter
        string = string[:-1]       #removes the last letter
        string2 = letter + reverse(string,string2) #creates a reverse string
        return string2 
    if length == 0:
        return string2[:-1]
string2 = reverse(string,string2) 
if string2 == string: 
    print("Palindrome!")
else : print("Not a palindrome!")


