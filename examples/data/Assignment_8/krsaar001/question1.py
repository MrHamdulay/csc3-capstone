# Aaron Krishna
# 5 May 2014
# A program to calculate whether or not a string is a palindrome

def palindrome(string): #funtion that checks is a string is a palindrome or not
    if len(string) < 2: 
        return True
    if string[0] != string[-1]: #base case
        return False
    return palindrome(string[1:-1]) #so I think you can guess that this is the recursive step (continually takes off first and last letter)

string = input("Enter a string:\n") 

if palindrome(string): #tells youn whether string is a palindrome or not
    print("Palindrome!")
else:
    print("Not a palindrome!")
    