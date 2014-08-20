
string = input("Enter a string:\n")

def palindrome(string):
    if len(string) == 0 or len(string) == 1:
        print ("Palindrome!")
    elif string[0] != string[len(string)-1]:
        print ("Not a palindrome!")
    elif string[0] == string[len(string)-1]:
        return palindrome(string[1:len(string)-1])
    
palindrome(string)