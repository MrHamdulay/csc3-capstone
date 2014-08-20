# a program with a recursive function to calculate whether or not a string is a palindrome 
#Jenny Luo
# 9 May 2014

string=input("Enter a string:\n")
#check to see if the string is an empty string and if it is not, check to see whether the first character and the last character are the same to decide if it is a palindrome
def palindrome(string):
    if(string != ""):
        recursive = string
        if recursive[0]==recursive[-1]:
            recursive=string[1:-1]
            return palindrome(recursive)# recursive statement
        else:
            return False
    else:
        return True
    
# display the final output    
if palindrome(string):
    print("Palindrome!")
else:
    print("Not a palindrome!")