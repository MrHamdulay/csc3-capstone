"""Checking for a palindrome
Richard Marais
9/05/14"""
def CheckPalindrome(palinstring,count):        #function with the string and a counting variable
    if (palinstring[count] == palinstring[len(palinstring)-count-1]         #if the final conditions are met print palindrome
        and count == len(palinstring)//2):
        print("Palindrome!")                      
    elif palinstring[count] == palinstring[len(palinstring)-count-1]:        #if the value of that point in the string = the corresponding point at the end of the string run the function for the next count value
        CheckPalindrome(palinstring,count+1)
    else:
        print("Not a palindrome!")       #if there is a mismatch print 'not palindrome'

inputstring = input("Enter a string:\n")
CheckPalindrome(inputstring,0)
