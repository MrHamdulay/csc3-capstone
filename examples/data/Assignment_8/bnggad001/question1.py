# Assignment 8: Question 1 
# Gadziraiushe Bangure: BNGGAD001
# May 9, 2014

# ----------------------------------------------------------------------
# A Python program with a recursive function to calculate whether or not a string is a palindrome (reads the sa me if reversed). You may NOT use iteration, string slicing or any other technique to reverse the string without using recursion!
# ----------------------------------------------------------------------

s = input('Enter a string:\n') #string input from the user
def palindrome (s):  
    
    if len(s)<=2 and s[0]==s[-1]:    #Base case
        return 'Palindrome!'
    elif s[0]!=s[-1]:
        return 'Not a palindrome!'
    else:
        return palindrome (s[1:-1])   #recursive call
print (palindrome (s))   #Print case