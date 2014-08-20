#program to tell if a string is a palindrome
#kiyarah pillay
#8 may 2014

#get input from user
string=input("Enter a string:\n")
def palindrome(string):
#base case
    if len(string) == 0:
#return an empty string
        return False
#if the first character is the same as the last character
    elif string [0] == string [-1]:
#call the function with a smaller, sliced string
#repeat process until we reach nought
        palindrome (string[1:-1])
        return True
def main ():
    if palindrome(string) == True:
        print ("Palindrome!")
    else:
        print ("Not a palindrome!")
main ()
        
        