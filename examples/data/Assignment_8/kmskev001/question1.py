"""checking for a palindrome
   kevin kumasamba
   05 may 2014"""

string=input("Enter a string:\n")

# problem: check to see if forward string is equal to backward string 
# smaller problem: check to see if forward character is equal to reverse character

def palindrome(string):
    if string=="":
        return "Palindrome!"
    elif string[0] == string[len(string)-1]:
            return palindrome(string[1:len(string)-1])
    else:
        return "Not a palindrome!"

print(palindrome(string))