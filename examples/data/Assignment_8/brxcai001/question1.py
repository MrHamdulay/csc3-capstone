# A Program to calculate whether an entered string is a palindrome.
# BRXCAI001
# 09 MAY 2014

string = input("Enter a string:\n")

def palindrome (string):
    #If the string is only 1 or 2 characters it is a Palindrome.
    if len(string) == 0 or len(string) ==1 :
        print("Palindrome!")
    #If the first letter of the string equals the last letter of the string then you move inward to check if the first and last letters correspond in the next string.
    elif string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        print ("Not a palindrome!")
palindrome(string)
    