"""This program takes a massage and checks whether it is a palindrome or not
Masilela Mduduzi
09 may 2014"""
def palindrome(string):
    if len(string)<=1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return palindrome(string[1:len(string)-1])
    
if __name__=='__main__':
    string = input("Enter a string:\n")
    #call the function palindrome
    if palindrome(string):
        print("Palindrome!")
    else:
        print("Not a palindrome!")
