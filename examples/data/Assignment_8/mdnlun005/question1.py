#-------------------------------------------------------------------------------
# Name:         question1
# Purpose:      program with a recursive function to calculate whether or not a
#               string is a palindrome (reads the sa me if reversed)
#
# Author:      Lungelo Mdunge
#
# Created:     04/05/2014
# Copyright:   (c) Lungelo 2014
#
#-------------------------------------------------------------------------------

pal=input("Enter a string:\n")

def palindrome(pal):
    if len(pal)==1 or pal=='':
        return "Palindrome!"

    elif pal[0]!=pal[-1]:
        return 'Not a palindrome!'

    else:
        return palindrome(pal[1:-1])
ans=palindrome(pal)
print(ans)

