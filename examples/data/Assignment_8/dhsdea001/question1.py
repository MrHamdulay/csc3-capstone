#Question 1
#Writing a palindrome check using recursion
#By: Dean de Haast

s = input("Enter a string:\n")

def palindrome(s):

    if s == "":
        return (print("Palindrome!"))
    else:
        if s[0] == s[-1]: #Checks the first and the last position to see if they have the same letter.
            return palindrome(s[1:-1]) # Recursive step, drops one letter on each end
        else:
            return (print("Not a palindrome!"))
        
palindrome(s)
