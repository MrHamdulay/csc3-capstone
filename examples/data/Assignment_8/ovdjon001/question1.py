""" Assingment 8, question1.py
by Jonathan Ovadia 
on 4th May 2014"""
def main():
    string = input("Enter a string:\n")
    if isPalindrome(string):
        print("Palindrome!")
    else:
        print("Not a palindrome!")

def isPalindrome(word):
    if len(word) == 1 or len(word)==0:
        return True 
    if word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    else:
        return False


if __name__ == "__main__": main()
