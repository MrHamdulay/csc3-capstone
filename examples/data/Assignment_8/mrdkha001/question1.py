"""Program to check whether palindrome or not
Khanyisile Morudu
06 May 2014""" 

#Input
String = input("Enter a string:\n")


#recursive function
def Palindrome_check(s):
    #if string is 1 then it's a true
    if len(s) < 2:
        return True
    #if the first s[0] and last s[-1] is not equal
    if s[0] != s[-1]:
        return False
    #checking again if middle parts are same, will send from after 1st and before last
    return Palindrome_check(s[1:-1])
    
#checking
if Palindrome_check(String) == True:
    #printing that it's true
    print("Palindrome!")
else:
    #printing that's it's not true
    print("Not a palindrome!")

