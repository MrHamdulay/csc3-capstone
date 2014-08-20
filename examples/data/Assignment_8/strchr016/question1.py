"""Checking for palindromes
Christopher Sterley
04/05/2014"""

def palindrome_checker(phrase,number):
    if number==-1:
        return ""
    else: return phrase[number] + palindrome_checker(phrase,number-1)
    
if __name__=='__main__':

    phrase=input("Enter a string:\n") #Get input from user

    

    number=len(phrase)-1 #create variable for splicing



    phrase_backward= palindrome_checker(phrase,number) #create variable of phrase backwards

    #determine whether the phrase is the same forward as it is backward
    if phrase==phrase_backward:
        print("Palindrome!")
    else:
        print("Not a palindrome!")

