# This is a Python program with a recursive function to calculate whether or not
# a string is a palindrome (reads the same if reversed). 

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 05 May 2014

def reverse_recursion(string):
    
    if string == "":
        return string # Base case: empty string
    else: # Recursively reverse the string
        return reverse_recursion(string[1:]) + string[0]
    
    
def main():
    
    phrase = input("Enter a string:\n")
    
    # Compare the phrase with a reversed copy of itself
    if phrase == reverse_recursion(phrase):
        print("Palindrome!")
    else:
        print("Not a palindrome!")


if __name__ == "__main__":
    main()

#Sample I/O:

#Enter a string:
#able was I ere I saw elba
#Palindrome!
#Sample I/O:

#Enter a string:
#elba is a noob
#Not a palindrome!