#Romello Naidoo
#NDXROM005
#9 May 2014
def palindrome(string):

    if len(string)<=2:
        return print("Palindrome!")
    else:
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        else:
            return print("Not a palindrome!")
        
string=input("Enter a string:\n")
palindrome(string)
