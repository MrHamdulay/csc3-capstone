# A program that tests for palindromes using recursion
# Martin Batek 
# 5 May 2014

def reverse(string):
    """A funtion that reverses a string using recursion"""
    if len(string) == 1:
        return string
    else:
        return string[len(string)-1] + reverse(string[:len(string)-1])

if __name__ == "__main__":
    users_input = input("Enter a string:\n") # Ask the user for their input
    if users_input == reverse(users_input):
        print("Palindrome!")
    else:
        print("Not a palindrome!")