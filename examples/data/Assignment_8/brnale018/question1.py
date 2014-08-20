# Alex Brunette
# 08/05/2014
# Programme to determine if a string is a palindrome


def palin(string):
    if string =='': #base case
        return string
    else:
        return palin(string[1:]) + string[0] #reverse string
    
string=input("Enter a string:\n") #get string from user
check_string = palin(string) #assigning reveresed string
if string == check_string: #checking if original string is the same as the reversed string
    print("Palindrome!")
elif string!= check_string:
    print("Not a palindrome!")
    