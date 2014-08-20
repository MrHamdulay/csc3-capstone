"""Assignment 8 question 1 receursive function for finding palidromes
Ross van der Heyde VHYROS001
7 May 2014"""

# function to reverse a string
def rev (word):
    """reverses the string supplied"""
    word = str(word)
    if len(word) == 1:
        return word
    else:
        return word[-1] + rev(word[:-1])
    
    
if __name__ == "__main__":
    x = input("Enter a string:\n")
    
    if x == rev(x):#compare string entered to its reversal
        print("Palindrome!")
    else:
        print("Not a palindrome!")
    
#Enter a string:
#able was I ere I saw elba
#Palindrome!
#Sample I/O:
#Enter a string:
#elba is a noob
#Not a palindrome!